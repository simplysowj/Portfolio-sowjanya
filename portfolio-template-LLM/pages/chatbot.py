__import__('pysqlite3')
import sys

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st
import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Streamlit app configuration
st.set_page_config(page_title='Resume Q&A Chatbot', layout='wide')

# Sidebar
st.sidebar.markdown("Developed by Sowjanya")
st.sidebar.markdown("Contact: [simplysowj@gmai.com](mailto:simplysowj@gmai.com)")
st.sidebar.markdown("GitHub: [Repo](https://github.com/simplysowj)")

# Main Title
st.title("Resume Q&A Chatbot")

# Input fields for the OpenAI API key
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Define the path to your local PDF file
pdf_file_path ="portfolio-template-LLM/images/Sowjanya_AI.pdf" 

# Text input for the question
question = st.text_input("Enter your question about the resume:")

# Define the fixed chain type and other configurations
chain_type = 'stuff'
chunk_size = 1000  # Fixed chunk size

def load_and_process_pdf(file_path):
    """Load and process the PDF to create a vector store."""
    # Load document from PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    # Create embeddings and vectorstore
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(texts, embeddings)
    
    return db

def get_qa_answer(query):
    """Generate the answer to the query using the QA chain."""
    # Ensure the API key is set
    os.environ["OPENAI_API_KEY"] = api_key

    # Process the PDF
    db = load_and_process_pdf(pdf_file_path)

    # Create retriever and QA chain
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})  # Using k=2 as an example
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(), chain_type=chain_type, retriever=retriever, return_source_documents=True
    )

    # Define the custom prompt
    name = "Sowjanya"
    pronoun = "her"
    prompt = f"""
    You are Buddy, an AI assistant dedicated to assisting {name} in her job search by providing recruiters with relevant and concise information. 
    If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}. 
    Don't put "Buddy" or a breakline in the front of your answer.
    """

    # Get the answer
    result = qa_chain({"query": query, "prompt": prompt})
    return result

if st.button("Run"):
    if api_key and question:
        with st.spinner("Processing..."):
            result = get_qa_answer(question)

        # Display the results
        st.write("**Answer:**")
        st.write(result["result"])

        
    else:
        st.error("Please provide all required inputs.")

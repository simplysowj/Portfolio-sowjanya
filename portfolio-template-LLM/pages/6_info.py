import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_text_splitters import NLTKTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from IPython.display import Markdown as md

st.title("🤖 RAG System on Leave No Context Behind Paper 📄")
user_input = st.text_input("Enter text ....")

# Initialize chat model
chat_model = ChatGoogleGenerativeAI(google_api_key="YOUR_GOOGLE_API_KEY", 
                                   model="gemini-1.5-pro-latest")

# Define chat template
chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="""You are a Helpful AI Bot. 
    You take the question from user and answer if you have the specific information related to the question. """),
    HumanMessagePromptTemplate.from_template("""Answer the following question: {question}
    Answer: """)
])

output_parser = StrOutputParser()

# Load PDF document
loader = PyPDFLoader(r"portfolio-template-LLM/images/Sowjanya_Data_science_latest_resume.pdf")
data = loader.load()

# Split documents into chunks
text_splitter = NLTKTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_documents(data)

# Create chunks embedding
embedding_model = GoogleGenerativeAIEmbeddings(google_api_key="YOUR_GOOGLE_API_KEY", 
                                               model="models/embedding-001")

# Store the chunks in vector store
db = Chroma.from_documents(chunks, embedding_model, persist_directory="./chroma_db_")
db.persist()

# Set up connection with the ChromaDB
db_connection = Chroma(persist_directory="./chroma_db_", embedding_function=embedding_model)

# Convert CHROMA db_connection to Retriever Object
retriever = db_connection.as_retriever(search_kwargs={"k": 5})

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Define chat template for RAG chain
chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="""You are a Helpful AI Bot. 
    You take the context and question from user. Your answer should be based on the specific context."""),
    HumanMessagePromptTemplate.from_template("""Answer the question based on the given context.
    Context:
    {context}
    
    Question: 
    {question}
    
    Answer: """)
])

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | chat_template
    | chat_model
    | output_parser
)

if st.button("Generate"):
    response = rag_chain.invoke(user_input)
    st.write(response)

import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import NLTKTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from IPython.display import Markdown as md
from langchain_community.document_loaders import PyPDFLoader
st.title("🤖 RAG System on Leave No Context Behind Paper 📄")
user_input = st.text_input("Enter text ....")

chat_model = ChatGoogleGenerativeAI(google_api_key="AIzaSyDvU3SwP_TMwEv_pfyy9JIqE_BMm4Y5O0Q", 
                                   model="gemini-1.5-pro-latest")


chat_template = ChatPromptTemplate.from_messages([
    # System Message Prompt Template
    SystemMessage(content="""You are a Helpful AI Bot. 
    You take the question from user and answer if you have the specific information related to the question. """),
    # Human Message Prompt Templatestrea
    HumanMessagePromptTemplate.from_template("""Aswer the following question: {question}
    Answer: """)
])


output_parser = StrOutputParser()

#Loading Document
loader = PyPDFLoader(r"bio.pdf")
pages = loader.load_and_split()

data = loader.load()

#splitting documents into chunkers

text_splitter = NLTKTextSplitter(chunk_size=500, chunk_overlap=100)

chunks = text_splitter.split_documents(data)
# Creating Chunks Embedding
embedding_model = GoogleGenerativeAIEmbeddings(google_api_key="AIzaSyDvU3SwP_TMwEv_pfyy9JIqE_BMm4Y5O0Q", 
                                               model="models/embedding-001")

# Store the chunks in vector store
db = Chroma.from_documents(chunks, embedding_model, persist_directory="./chroma_db_")
db.persist()
# Setting a Connection with the ChromaDB
db_connection = Chroma(persist_directory="./chroma_db_", embedding_function=embedding_model)
# Converting CHROMA db_connection to Retriever Object
retriever = db_connection.as_retriever(search_kwargs={"k": 5})
#retrieved_docs = retriever.invoke(user_input)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


chat_template = ChatPromptTemplate.from_messages([
    # System Message Prompt Template
    SystemMessage(content="""You are a Helpful AI Bot. 
    You take the context and question from user. Your answer should be based on the specific context."""),
    # Human Message Prompt Template
    HumanMessagePromptTemplate.from_template("""Aswer the question based on the given context.
    Context:
    {context}
    
    Question: 
    {question}
    
    Answer: """)
])
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | chat_template
    | chat_model
    | output_parser
)



if st.button("Genrate"):
    response = rag_chain.invoke(user_input)
    st.write(response)

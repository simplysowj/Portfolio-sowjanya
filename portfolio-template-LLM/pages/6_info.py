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



st.markdown(
    """
    ### About Sowjanya:
    Sowjanya is a seasoned professional with expertise in AI, Data Science technologies. Holding a Post grad degree in data Science from the University of Chandigarh (2024), Sowjanya is committed to delivering innovative solutions.

    ### Work Experience:
    Data Science Intern and a Final year student

    ### Career Goal:
    Sowjanya's career goal is to leverage their expertise in AI and emerging technologies to drive meaningful innovation and create solutions that positively impact businesses and society.

    ### Skills: 
    AI, Data Science, Web technologies, Python, React JS, Spring Boot, and Big Data engineering

    ### Certification:
    - Certified Data Scientist

    ### Achievements:
    - LOR for the Internship

    ### Contact:
    - [LinkedIn](https://www.linkedin.com/in/sowjanya-bojja/)
    - Phone: 6692974674
    - Location: USA

    ### Strengths and Advantages:
    Sowjanya's strengths lie in a profound passion for technology, innovative problem-solving, and client-centric solutions.

    ### Weaknesses and Disadvantages:
    Sowjanya's unwavering pursuit of excellence may occasionally lead to in-depth analysis, but it ensures the delivery of high-quality services.

    ### Interests and Hobbies:
    Sowjanya's passion for technology extends into leisure hours, where they delve into the cutting-edge realm of GenAI, continuously pushing the boundaries of what can be achieved in various projects. In addition, she finds joy in the simple pleasures of life, solving puzzles, playing chess, and listening to music.

    ### Portfolio:
    Explore Sowjanya's portfolio, showcasing expertise and tailored solutions. This website also serves as a showcase for some of Sowjanya's remarkable projects. Constructed using generative AI and Python, the website aims to inspire visitors with innovative ideas on seamlessly integrating generative AI into their own portfolio websites. Feel free to explore and ignite your creativity!

    ### Availability:
    Sowjanya is actively seeking new opportunities and is ready to start immediately.

    ### References:
    References are available upon request.

    ### Certifications:
    - Certified Data Scientist
    - Certified Machine Learning Specialist

    ### Projects:
    - Fraud Detection System using LSTM Autoencoders and Spark-Kafka Integration.
    - Real-time Analytics Dashboard using Streamlit and Plotly.

    ### Publications:
    - Article on Machine Learning Best Practices, Medium.
    - Research Paper on Anomaly Detection, IEEE.

    ### Hobbies:
    - Blogging about data science and machine learning.
    - Participating in hackathons and coding competitions.

    ### Education:
    - M.S.C in Data Science
    """, unsafe_allow_html=True
)

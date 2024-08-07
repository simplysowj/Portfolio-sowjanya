import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from constant import *
from PIL import Image
import openai
from langchain.chat_models import ChatOpenAI

import json

img_1 = Image.open("portfolio-template-LLM/images/bd.png")
img_2 = Image.open("portfolio-template-LLM/images/mdb.png")
img_3 = Image.open("portfolio-template-LLM/images/gai.png")
img_4 = Image.open("portfolio-template-LLM/images/t.png")

img_4=img_4.resize((70, 70))
img_3=img_3.resize((70, 70))
st.set_page_config(page_title='Template' ,layout="wide",page_icon='👧🏻')


pdf_path = "portfolio-template-LLM/images/Resume_Sowjanya_DataScience_New1.pdf"




# Provide a download button for the PDF
with open(pdf_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()
    st.download_button(
        label="Download Resume as PDF",
        data=pdf_bytes,
        file_name="Sowjanya_Data_science_latest_resume.pdf",
        mime="application/pdf"
    )

# Custom CSS for the download button
st.markdown("""
    <style>
    .stDownloadButton > button {
        background-color: #d0a3f0; 
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        border: none;
    }
    .stDownloadButton > button:hover {
        background-color: #d0a3f0;
    }
    </style>
    """, unsafe_allow_html=True)

# -----------------  chatbot  ----------------- #

st.sidebar.markdown("Developed by Sowjanya")
st.sidebar.markdown("Contact: [simplysowj@gmai.com](mailto:simplysowj@gmai.com)")
st.sidebar.markdown("GitHub: [Repo](https://github.com/simplysowj)")

st.sidebar.markdown(
        """
        <style>
        /* Style the sidebar itself */
        [data-testid=stSidebar] {
            background-image: linear-gradient(#cfbae2, #cfbae2);
            
        }

        /* Style hyperlinks */
        .sidebar-content a {
            display: block;
            color: #2e9aff !important;
            font-weight: bold;
        }

        /* Style paragraphs */
        .sidebar-content p {
            color: white;
        }

        /* Set text color for the entire sidebar */
        .sidebar-content, .sidebar-content * {
            color: white !important;
        }

        /* Customize caret color */
        .st-ck {
            caret-color: black;
        }

        /* Set text color for certain elements */
        .st-bh, .st-c2, .st-c3, .st-c4, .st-c5, .st-c6, .st-c7, .st-c8, .st-c9, .st-ca, .st-cb, .st-b8, .st-cc, .st-cd, .st-ce, .st-cf, .st-cg, .st-ch, .st-ci, .st-cj, .st-ae, .st-af, .st-ag, .st-ck, .st-ai, .st-aj, .st-c1, .st-cl, .st-cm, .st-cn {
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
st.markdown(
        """
        <style>
        .container {
            max-width: 800px;
        }
        .title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .description {
            margin-bottom: 30px;
        }
        .instructions {
            margin-bottom: 20px;
            padding: 10px;
            background-color: #f5f5f5;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# load the file
file_path = "portfolio-template-LLM/bio.txt" 
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()



#pronoun = info["Pronoun"]
#name = info["Name"]


info = {
    "Pronoun": "she",
    "Name": "Sowjanya",
    "Full_Name": "Sowjanya Bojja",
    "Intro": "A Data Scientist passionate about leveraging data to drive insights.",
    "About": "Experienced in Machine Learning, Data Analysis, and Data Visualization.",
    "Email": "simplysowj@gmai.com"
}
pronoun = info["Pronoun"]
name = info["Name"]




# Function to create a horizontal navbar
def horizontal_navbar(links):
    nav_html = """
    <style>
    .navbar {
        overflow: hidden;
        background-color: #d0a3f0;
        display: flex;
        justify-content: center;
    }

    .navbar a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
        font-size: 17px;
    }

    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
    </style>
    <div class="navbar">
    """
    for link in links:
        nav_html += f'<a href="{link["url"]}" {"download" if link["label"] == "Resume" else ""}>{link["label"]}</a>'
    nav_html += "</div>"
    return nav_html

# Define links for the navbar
navbar_links = [
    {"label": "Medium Article", "url": "https://medium.com/@simplysowj"},
    
    {"label": "LinkedIn", "url": "https://www.linkedin.com/in/sowjanya-bojja/"},
    {"label": "GitHub", "url": "https://github.com/simplysowj"},
   
]

# Render the horizontal navbar
st.markdown(horizontal_navbar(navbar_links), unsafe_allow_html=True)

# Set up the OpenAI key

openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key and hit Enter', type="password")
openai.api_key = (openai_api_key)
st.markdown("## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) in the sidebar🔑\n"  # noqa: E501
        )



def ask_bot(input_text):
    # define LLM
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=openai.api_key,
    )
    llm_predictor = LLMPredictor(llm=llm)
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    
    # load index
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)    
    
    # query LlamaIndex and GPT-3.5 for the AI's response
    PROMPT_QUESTION = f"""You are Buddy, an AI assistant dedicated to assisting {name} in her job search by providing recruiters with relevant and concise information. 
    If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}. 
    Don't put "Buddy" or a breakline in the front of your answer.
    Human: {input}
    """
    
    output = index.as_query_engine().query(PROMPT_QUESTION.format(input=input_text))
    print(f"output: {output}")
    return output.response

# get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("After providing OpenAI API Key on the sidebar, you can send your questions and hit Enter to know more about me from my AI agent, Buddy! Meanwhile you can explore sidebar for her certifications,internships,resume,hobbies etc", key="input")
    return input_text

#st.markdown("Chat With Me Now")
user_input = get_text()

if user_input:
  #text = st.text_area('Enter your questions')
  if not openai_api_key.startswith('sk-'):
    st.warning('⚠️Please enter your OpenAI API key on the sidebar.', icon='⚠')
  if openai_api_key.startswith('sk-'):
    st.info(ask_bot(user_input))

# -----------------  loading assets  ----------------- #

    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def load_lottie_json(file_path: str):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading Lottie JSON file: {e}")
        return None

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    
local_css("portfolio-template-LLM/style/style.css")
lottie_files = {
    'ai': 'portfolio-template-LLM/images/AI.json',
    'react':'portfolio-template-LLM/images/React.json',
    'mongo':'portfolio-template-LLM/images/mongo.json'}
lottie_animations = {key: load_lottie_json(path) for key, path in lottie_files.items()}
# loading assets
ai = load_lottie_json('portfolio-template-LLM/images/AI.json')
react = load_lottie_json('portfolio-template-LLM/images/React.json')
mongo = load_lottie_json('portfolio-template-LLM/images/mongo.json')
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")

st.sidebar.image("portfolio-template-LLM/images/profile.jpg", width=150, caption="Profile Picture")
# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm Sowjanya👋", info["Intro"])
    st.write("")
    st.write(info['About'])
    
    
with col2:
    st_lottie(lottie_gif, height=280, key="data")
        

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=100,width=100, key="python", speed=2.5)
    with col2:
        st_lottie(java_lottie, height=100,width=100, key="java", speed=4)
    with col3:
        st_lottie(my_sql_lottie,height=100,width=100, key="mysql", speed=2.5)
    with col4:
        st_lottie(git_lottie,height=100,width=100, key="git", speed=2.5)
    with col1:
        st_lottie(github_lottie,height=60,width=60, key="github", speed=2.5)
    with col2:
        st_lottie(docker_lottie,height=100,width=100, key="docker", speed=2.5)
  
    with col3:
        st_lottie(lottie_animations['ai'], height=100, width=100, key="ai")
    with col4:
        st_lottie(lottie_animations['react'], height=70, width=70, key="react")
    with col1:
            st.image(img_1 )
    with col2:
        st_lottie(lottie_animations['mongo'], height=100, width=100, key="mongo")
    with col3:
            st.image(img_3 )
    with col4:
            st.image(img_4 )
    

    # Technical Skills Section
    st.subheader("🛠 Technical Skills")
 
    st.markdown("""
                <div style=" padding: 10px; border-radius: 5px;">
                    <ul style="list-style-type: none; padding: 0;">
                        <li><b>Programming Languages:</b> Python, Java, C</li>
                        <li><b>Web Development:</b> HTML, CSS, JavaScript, Bootstrap</li>
                        <li><b>JavaScript Libraries & Frameworks:</b> Node.js, React.js</li>
                        <li><b>Java Framework:</b> SpringBoot</li>
                        <li><b>Microservices & Containers:</b> Docker</li>
                        <li><b>Big Data Engineering:</b> Kafka, PySpark</li>
                        <li><b>Gen AI Skills:</b> LLM (Large Language Model)</li>
                        <li><b>Data Visualization:</b> Tableau, Excel, Matplotlib, Seaborn</li>
                        <li><b>Web Frameworks:</b> Flask, Streamlit</li>
                        <li><b>GUI Development:</b> Swing</li>
                        <li><b>Other Technologies:</b> Microservices Architecture</li>
                        <li><b>Tools:</b> Git, Anaconda, Jupyter notebook/Colab, VS Code, IntelliJ IDEA</li>
                        <li><b>Databases:</b> MySQL, PostgreSQL, Toad, MongoDB Atlas</li>
                        <li><b>Soft Skills:</b> Problem Solving, Team Collaboration, Communication, Time Management</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
   # Education Section
    st.subheader("🎓 Education")
    st.write("""
              -**Master of Science (MSC) in Data Science Chandigarh University, India  July 2022 - August 2024**
               -**Relevant Coursework **: Python Programming, Calculus and Linear Algebra, Applied Probability and Statistics, 
                  Data Analysis and Visualization, Communication and Soft Skills, Machine Learning, SQL Programming, 
                  Advanced Machine Learning, Advanced Database Management, Deep Learning, Optimization, Natural Language Processing,
                  Web Technologies,Cloud Native Development,Java Programming,Data Structures and algorithms,NLP,
                  Applied Business Analytics,Data Mining and Data warehousing,data Engineering.
              - **Academic Projects & Papers **:
                Academic Papers
                https://medium.com/@simplysowj
                
                Big Data Engineering and Gen AI Project(Kafka,Pyspark via Zeppelin using Docker) 
                Sentiment Analysis
                https://github.com/simplysowj/bigdataenggproject
                Implemented a fraud detection system using big data concepts such as Kafka, PySpark, and MySQL with Machine learning algorithms. 
                Developed a user-friendly interface using Streamlit and incorporated Gen AI for front-end enhancement.
                https://github.com/simplysowj/bigdata_fraud_detection
                Image Captioning with OCR and GenAI
                Developed an interactive chatbot capable of generating captions for images and audio with Text in the image.
                Utilized advanced AI techniques, 
                including image captioning (using Deep learning and NLP) and audio generation with Gen AI, to enhance user experience.
                 https://github.com/simplysowj/OCR_Imagecaptioning_openai
                 EDA with DataBricks
                worked on a project where I analyzed sales data using Databricks, hashtag#PySpark, and hashtag#Matplotlib.
                https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/1123303988966450/1736356871005362/5428641177518963/latest.html
               Movie Review App
                Developed a movie review application using MongoDB, 
                Java, Spring Boot, and React, featuring a loosely coupled architecture for independent evolution 
                of client and server code, leveraging microservices for efficient business function handling.
                Spring Boot was chosen for its rapid development capabilities in the microservices landscape.
               https://github.com/simplysowj/Microservices
               
            -**Bachelor of Technology (B. Tech) in Electronics and Communications –JNTU, India.    2002 - 2006**

            """)
            
   # Advanced Skills Section
    st.subheader("🔍 Advanced Skills")
    st.write("""
            - **Machine Learning & Deep Learning**:
              - **Libraries**: NumPy, Pandas, Scikit-learn, NLTK, TensorFlow, PyTorch
              - **Techniques**: Data Exploration & Analysis, Data Modelling, Statistics and Probability, Linear Regression, Gradient Descent, Logistic Regression, Regularization, SVM, KNN, Decision Trees, Random Forest, Ensemble Techniques, Bagging & Boosting, Cross-Validation, Cluster Analysis, Hyperparameter Tuning, Experiment Tracking and Model Management using MLflow, MLOps
              - **NLP Techniques**: Tokenization, Bag of Words, Stemming, Lemmatization, POS Tagging, TF-IDF, BERT, Word2Vec, GloVe
              - **Deep Learning**: Neural Network Architectures (CNN, RNN, LSTM), Computer Vision (Image Classification, Object Detection, Image Segmentation), NLP Tasks (Sentiment Analysis, Text Classification, Language Modeling, Generative Adversarial Networks), Optimization Techniques (Gradient Descent)
            """)
    
    
    #Industry Experience:
    st.subheader("Previous Industry Experience in TCS , India")
    st.write("""
            -**Plsql Developer Tools**:
                   TOAD 7.6.0.11, PL/SQL Developer, Forms 61, Reports 6i
            -**Company TCS**:
                -**Client**: Electronic Arts-India Location Bangalore, India (2010 to 2014) (Nov 2010 May2014)
                -**Client**: Tata TeleServices Limited - India (2008 to 2010) Mar 2008-Oct 2010
             """)
     


# -----------------  contact  ----------------- #
    with col2:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

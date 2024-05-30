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


st.set_page_config(page_title='Template' ,layout="wide",page_icon='👧🏻')


# -----------------  chatbot  ----------------- #
# Set up the OpenAI key
openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key and hit Enter', type="password")
openai.api_key = (openai_api_key)
st.markdown("## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) in the sidebar🔑\n"  # noqa: E501
        )

# load the file
file_path = "portfolio-template-LLM/bio.txt" 
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()


pronoun = info["Pronoun"]
name = info["Name"]
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
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)
st.sidebar.markdown(info['Github'],unsafe_allow_html=True)
    
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
    'react':'portfolio-template-LLM/images/React.json'}
lottie_animations = {key: load_lottie_json(path) for key, path in lottie_files.items()}
# loading assets
ai = load_lottie_json('portfolio-template-LLM/images/AI.json')
react = load_lottie_json('portfolio-template-LLM/images/React.json')
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
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])
    
    
with col2:
    st_lottie(lottie_gif, height=280, key="data")
        

# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
    with col2:
        st_lottie(java_lottie, height=70,width=70, key="java", speed=4)
    with col3:
        st_lottie(my_sql_lottie,height=70,width=70, key="mysql", speed=2.5)
    with col4:
        st_lottie(git_lottie,height=70,width=70, key="git", speed=2.5)
    with col1:
        st_lottie(github_lottie,height=50,width=50, key="github", speed=2.5)
    with col2:
        st_lottie(docker_lottie,height=70,width=70, key="docker", speed=2.5)
  
    with col3:
        st_lottie(lottie_animations['ai'], height=100, width=100, key="ai")
    with col4:
        st_lottie(lottie_animations['react'], height=50, width=50, key="react")
    with col1:
            st.image(img_1 ,width=50, height=50)
    with col2:
            st.image(img_2 ,width=50, height=50)
    with col3:
            st.image(img_3 ,width=50, height=50)
    with col4:
            st.image(img_4 ,width=50, height=50)
    

    # Technical Skills Section
    st.subheader("🛠 Technical Skills")
 
    st.markdown("""
                <div style="background-color: #f9f9f9; padding: 10px; border-radius: 5px;">
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
            - **MSC in Data Science**:
              - **University**: Chandigarh University
              - **Subjects**: Python Programming, Calculus and Linear Algebra for Data Scientists, Applied Probability and Statistics, Data Analysis and Visualization, Communication and Soft Skills, Machine Learning, SQL Programming, Advanced Machine Learning, Advanced Database Management, Deep Learning, Optimization, Natural Language Processing
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

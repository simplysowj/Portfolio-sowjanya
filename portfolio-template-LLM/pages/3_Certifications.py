import streamlit as st
from PIL import Image
from constant import *

        



img_4 = Image.open("portfolio-template-LLM/images/4.png")
img_5 = Image.open("portfolio-template-LLM/images/5.png")
img_6 = Image.open("portfolio-template-LLM/images/6.png")
img_7 = Image.open("portfolio-template-LLM/images/7.png")
img_8 = Image.open("portfolio-template-LLM/images/8.png")
img_9 = Image.open("portfolio-template-LLM/images/9.png")
img_10 = Image.open("portfolio-template-LLM/images/nlp.png")

st.title("🫶 Certifications")

col1, col2, col3,col4,col5,col6 = st.columns(6)

st.image(img_4)
   
st.image(img_5)

st.image(img_6)
st.image(img_7)
   
st.image(img_8)
st.image(img_9)
st.image(img_10)

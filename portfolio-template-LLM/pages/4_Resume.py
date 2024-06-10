import streamlit as st
import base64
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
#local_css("portfolio-template-LLM/style/style.css")

st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

st.title("📝 Resume")

pdf_path = "portfolio-template-LLM/images/Sowjanya_Data_science_latest_resume.pdf"

# Provide a download button for the PDF
with open(pdf_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()
    st.download_button(
        label="Download Resume as PDF",
        data=pdf_bytes,
        file_name="Sowjanya_Data_science_latest_resume.pdf",
        mime="application/pdf"
    )

# Inform users about the download button
st.markdown(
    """
    Click the button above to download the resume as a PDF file.
    """,
    unsafe_allow_html=True
)

with open("portfolio-template-LLM/images/Sowjanya_Data_science_latest_resume.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
  

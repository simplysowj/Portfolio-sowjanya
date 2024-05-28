import streamlit as st
import base64

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("portfolio-template-LLM/style/style.css")

#st.sidebar.markdown(info['Photo'], unsafe_allow_html=True)

st.title("📝 Resume")

# Read the PDF file
pdf_path = "portfolio-template-LLM/images/Sowjanya_Data_science_latest_resume.pdf"
with open(pdf_path, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
    
# Display the PDF
st.markdown(pdf_display, unsafe_allow_html=True)

# Add a download button for the PDF
with open(pdf_path, "rb") as f:
    pdf_bytes = f.read()

st.download_button(
    label="Download PDF",
    data=pdf_bytes,
    file_name="Sowjanya_Data_science_latest_resume.pdf",
    mime="application/pdf",
)


import streamlit as st

#st.sidebar.markdown(info['Photo'], unsafe_allow_html=True)

st.title("📝 Resume")

# Path to the PDF file
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

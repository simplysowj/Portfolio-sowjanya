import streamlit as st

def display_projects():
    st.title("My Projects")

    projects = [
        {
            "title": "AI Intern, Mentorness",
            "duration": "Feb 2024 - Mar 2024",
            "description": """
            Developed a dynamic ATS Resume Expert application using Gemini-pro-vision during my internship with Mentorness. 
            Utilizing OpenAI's Generative AI capabilities, it analyzes PDF resumes against job descriptions, offering evaluations on alignment, 
            missing keywords, and candidate suitability. This Streamlit app showcases a versatile portfolio template integrating features like 
            resume parsing, an AI chatbot powered by OpenAI, and interactive elements for comprehensive personal branding, demonstrating 
            proficiency in leveraging diverse technologies for impactful web experiences.
            """,
            "github_link": "https://github.com/simplysowj/Mentorness",
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_atsresume-streamlit-resumeparser-activity-7173455333477064704-WaeO?utm_source=share&utm_medium=member_desktop"  
        },
        {
            "title": "Bharat Intern - Data Science Intern",
            "duration": "Jan 2024 - Feb 2024",
            "description": """
            Implemented an SMS spam/ham classifier leveraging machine learning techniques to accurately classify text messages. 
            Additionally, developed a Titanic data classification model to predict survival outcomes using passenger data.
            """,
            "github_link": "https://github.com/simplysowj/CatVsDog_Classifier-SpamDetector",
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_internship-journey-with-bharat-intern-sms-activity-7164659747697205248-sOjj?utm_source=share&utm_medium=member_desktop"
        },
        # Add more projects as needed
    ]

    for project in projects:
        st.subheader(project["title"])
        st.write(f"**Duration:** {project['duration']}")
        st.write(project["description"])
        if project["github_link"]:
            st.write(f"[GitHub Repository]({project['github_link']})")
        if project["video_link"]:
            st.write(project["video_link"])


display_projects()

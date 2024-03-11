import streamlit as st
import requests
import json
import os
import fitz  # PyMuPDF

def set_page_bg_color():
    st.markdown("""
    <style>
    .stApp {
        background-color: #129783;
    }
    </style>
    """, unsafe_allow_html=True)

set_page_bg_color() 

# Function to extract text from PDF
def extract_text_from_pdf(pdf_content):
    with st.spinner('Extracting text from PDF...'):
        try:
            with fitz.open(stream=pdf_content, filetype="pdf") as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
            return text
        except Exception as e:
            st.sidebar.error(f"Failed to extract text from PDF: {e}")
            return None

# Function to send the user's question and the document to the API and return the response
def get_answer(user_question, Rubrics, Question, Answer):
    url = "https://api.vectorshift.ai/api/pipelines/run"
    
    headers = {
        "Public-Key": str(st.secrets["PUBLIC_KEY"]),
        "Private-Key": str(st.secrets["PRIVATE_KEY"]),
    }

    print(st.secrets["PUBLIC_KEY"])
    print(st.secrets["PRIVATE_KEY"])

    body = {
        "inputs": json.dumps({
            "User_Question": user_question, 
            "Rubrics": Rubrics, 
            "Question": Question, 
            "Answer": Answer
        }),
        "pipeline_name": "Code Grader",
        "username": "ajanraj",
    }
    
    with st.spinner('Grading Assignment...'):
        try:
            response = requests.post(url, headers=headers, json=body)
            if response.status_code == 200:
                return response.json()
            else:
                st.sidebar.error(f"API call failed with status code {response.status_code}: {response.text}")
                return None
        except Exception as e:
            st.sidebar.error(f"Failed to make API call: {e}")
            return None


# Custom CSS to set the title size and possibly color or other properties
def custom_title(text, font_size='5em'):  # Adjust '3em' as needed
    st.markdown(f"""
    <style>
    .big-title {{
        font-size: {font_size};
        font-weight: bold;
        font-family: Bskerville Old Face;
        text-align: justify;
        color: #FFF8DC;
    }}
    </style>
    <p class='big-title'>{text}</p>    
    """, unsafe_allow_html=True)

# Use the function to display your title with a larger size
custom_title('Smart Assess')

with st.container():
    user_question = st.text_input("Enter your question:")
    col1, col2, col3 = st.columns(3)
    with col1:
        Rubrics = st.file_uploader("Upload the Rubrics", type=["pdf"], help="PDF file for Rubrics")
    with col2:
        Question = st.file_uploader("Upload the Question", type=["pdf"], help="PDF file for Question")
    with col3:
        Answer = st.file_uploader("Upload the Answer", type=["pdf"], help="PDF file for Answer")
    

if st.button('Grade Assignment'):
    if all([Rubrics, Question, Answer, user_question]):
        Rubrics_text = extract_text_from_pdf(Rubrics.getvalue()) if Rubrics else ""
        Question_text = extract_text_from_pdf(Question.getvalue()) if Question else ""
        Answer_text = extract_text_from_pdf(Answer.getvalue()) if Answer else ""
        
        if all([Rubrics_text, Question_text, Answer_text]):
            answer = get_answer(user_question, Rubrics_text, Question_text, Answer_text)
            if answer and "output_1" in answer:
                st.markdown(f"**Grade Result:**\n{answer['output_1']}", unsafe_allow_html=True)
                st.success("Successfully Graded the Assignment!")
            else:
                st.sidebar.error("No answer returned from the API.")
        else:
            st.sidebar.error("Failed to extract text from one or more documents.")
    else:
        st.sidebar.warning("Please fill in all fields and upload all required documents to proceed.")

st.divider()

# Updated section with larger font
st.markdown("""
<style>
.big-font {
    font-size:25px !important;
    font-family: Bskerville Old Face;
    text-align: justify;
    color: #FFF8DC;
}
</style>
<div class="big-font">
Experience Smart Assess: a cutting-edge web app revolutionizing grading. Upload question papers, rubrics and mark student answers seamlessly. Intuitive and user-friendly, it's your key to efficiency and accuracy in grading. Say goodbye to tedious manual grading and hello to efficiency and accuracy like never before.
</div>
""", unsafe_allow_html=True)
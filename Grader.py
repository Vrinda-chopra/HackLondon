import streamlit as st
import requests
import json
import fitz  # PyMuPDF

# Function to extract text from PDF
def extract_text_from_pdf(pdf_content):
    with fitz.open(stream=pdf_content, filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

# Function to send the user's question and the document to the API and return the response
def get_answer(user_question, Rubrics, Question, Answer):
    url = "https://api.vectorshift.ai/api/pipelines/run"
    
    headers = {
        "Public-Key": "VVMlga4AaQxB7wMBuOMsQH5OhLWrtaBAs_K2aJ-hbcw",
        "Private-Key": "B_hEa-vpWAmrOnVs9atZ40TKv9H-EvnCD64qeIZfO9I",
    }

    body = {
    "inputs": json.dumps({"User_Question": user_question, "Rubrics": Rubrics, "Question": Question, "Answer": Answer}),
    "pipeline_name": "Code Grader",
        "username": "ajanraj",
    }
    
    response = requests.post(url, headers=headers, data=body)
    print(response)
    return response.json()


# Streamlit app
st.title('Assignment Grader')

# Create a text input box for the user's question
user_question = st.text_input("Enter your question:")

# Create a file uploader for PDF documents
Rubrics = st.file_uploader("Upload the Rubrics", type=["pdf"])

Question = st.file_uploader("Upload the Question", type=["pdf"])

Answer = st.file_uploader("Upload the Answer", type=["pdf"])

# Check if a file was uploaded
if Rubrics is not None:
    # Extract text from the uploaded PDF
    Rubrics_text = extract_text_from_pdf(Rubrics.getvalue())

    Question_text = extract_text_from_pdf(Question.getvalue())

    Answer_text = extract_text_from_pdf(Answer.getvalue())
    
    # Button to submit the question and document
    if st.button('Get Answer'):
        # Call the function to get the answer
        answer = get_answer(user_question, Rubrics_text, Question_text, Answer_text)
        print(answer)
        
        # Display the answer
        if "output_1" in answer:
            st.write(answer["output_1"])
        else:
            st.write(answer)

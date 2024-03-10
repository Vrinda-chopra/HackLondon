# Smart Assess

Smart Assess is a Streamlit application designed to grade assignments by comparing student submissions against given rubrics. This application leverages the `vectorshift.ai` API to evaluate answers based on the criteria specified in the rubrics document.

## Features

- Upload PDF documents for rubrics, questions, and student answers.
- Enter specific questions for more directed grading insights.
- Receive grading insights directly through the Streamlit interface.

## Installation

To run this application, you'll need Python installed on your machine. This application requires the following Python libraries: `streamlit`, `requests`, `fitz` (PyMuPDF), and `json`. You can install these dependencies using pip:

```bash
pip install streamlit requests PyMuPDF
```

## Running the Application

1. Clone this repository to your local machine or download the provided `.py` file directly.
2. Navigate to the directory containing the application file in your terminal.
3. Run the application with Streamlit:

```bash
streamlit run Grader.py
```

## Usage

After running the application, the Streamlit interface will guide you through the following steps:

1. **Enter Your Question:** Type in a specific question or instruction regarding the assignment grading.
2. **Upload the Rubrics:** Upload a PDF document containing the grading rubrics.
3. **Upload the Question:** Upload the PDF document containing the assignment questions.
4. **Upload the Answer:** Upload the PDF document containing the student's answers.
5. Click on `Grade Assignment` to submit the information and receive grading insights.

The application will then display the grading insights based on the provided documents and question.

## API Keys

This application requires valid `Public-Key` and `Private-Key` provided by `vectorshift.ai`. Ensure you replace the placeholder keys in the application code with your actual API keys to use the grading functionality.

## Contributing

Contributions to the Assignment Grader application are welcome. If you have suggestions for improving this application, please feel free to fork the repository and submit a pull request.

## Contact

For any queries or further assistance, please reach out through [GitHub Issues](https://github.com/SavaniSawaikar/HackLondon/issues) on the project repository.

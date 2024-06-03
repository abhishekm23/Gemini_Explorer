# Gemini_Explorer
A Python web application for having an interactive conversation with Google Gemini model. 
Gemini Explorer is a simple Python web application that allows us as the user to interface with an AI algorithm using the Google Gemini model. The purpose of this project is to become familiar with the fundamentals of using Google Gemini with the Streamlit library. So here we have integrated Gemini into our Python code using Streamlit library to create an Web App AI chat interface. Here Gemini is an API, where we need to have Gcloud account to access it. Moreover, vertexAI is a library that provided us with various Gemini-versions, but here in our case we use Gemini-pro for this project.

## Requirements
python version 3.11x 
streamlit
Gcloud account
vertexai 

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv env # to create env
   OR  .\env\Scripts\Activate  # On Windows
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run gem_exp.py
   ```

## Usage

- Open the app in your browser.
- Enter your name to start interacting with ReX, the AI assistant.
- ReX will provide personalized responses based on your inputs.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License.

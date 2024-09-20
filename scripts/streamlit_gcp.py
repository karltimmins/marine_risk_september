import streamlit as st
import os
import vertexai # type: ignore
from vertexai.generative_models import GenerativeModel # type: ignore
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')

load_dotenv(dotenv_path)

# Initialize Vertex AI
PROJECT_ID = os.environ.get("GCP_PROJECT")
MODEL_ID = "gemini-1.5-flash-001"
vertexai.init(project=PROJECT_ID, location="us-central1")

# Load the model
model = GenerativeModel(MODEL_ID)

# Streamlit app
st.title("Risk Assessment - Accenture")

# Input from the user
user_input = st.text_input("Enter a prompt for the story:")

# Generate content when the button is clicked
if st.button("Generate Story"):
    if user_input:
        response = model.generate_content(user_input)
        st.write("### Generated Story")
        st.write(response.text)
    else:
        st.write("Please enter a prompt to generate a story.")
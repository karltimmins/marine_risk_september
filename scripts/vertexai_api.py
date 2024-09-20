import os
from os.path import join, dirname
from dotenv import load_dotenv
import vertexai
import json
from vertexai.generative_models import GenerativeModel

dotenv_path = join(dirname(__file__), '.env')

load_dotenv(dotenv_path)

with open('./training_data.json', 'r') as file:
    textData = json.load(file)

# Initialize Vertex AI
PROJECT_ID = os.environ.get("GCP_PROJECT")
MODEL_ID = "gemini-1.5-flash-001"
TEXT = textData

vertexai.init(project=PROJECT_ID, location="us-central1")

model = GenerativeModel("gemini-1.5-flash-001")

response = model.generate_content(
    "What is the name of the planets in our solar system?"
)

print(response.text)
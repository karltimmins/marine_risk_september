import os
from os.path import join, dirname
from dotenv import load_dotenv
import vertexai
import json
from vertexai.generative_models import GenerativeModel

file_path = r"C:/Users/Karl.timmins/projects/GenAI_2024/marine_risk/training_data.json"

# Open the file and load the JSON data
with open(file_path, 'r') as file:
    data = json.load(file)

dotenv_path = join(dirname(__file__), '.env')

load_dotenv(dotenv_path)

# Initialize Vertex AI
PROJECT_ID = os.environ.get("GCP_PROJECT")
MODEL_ID = "gemini-1.5-flash-001"

# Convert the data to a string format if necessary
data_str = json.dumps(data)

vertexai.init(project=PROJECT_ID, location="us-central1")

model = GenerativeModel("gemini-1.5-flash-001")

response = model.generate_content(
f"From the data provided what can you gather? The data represents shipping container data and related to dates, routes taken and cargo, incidents and cargo data={data_str}"
)

print(response.text)
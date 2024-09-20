import os
from os.path import join, dirname
from dotenv import load_dotenv
from vertexai.preview.language_models import TextEmbeddingModel, TextEmbeddingInput
import json

file_path = r"C:/Users/Karl.timmins/projects/GenAI_2024/marine_risk/training_data.json"

# Open the file and load the JSON data
with open(file_path, 'r') as file:
    data = json.load(file)

# Load environment variables from .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Initialize Vertex AI
PROJECT_ID = os.environ.get("GCP_PROJECT")
MODEL_ID = "text-embedding-004"

task_type = "RETRIEVAL_DOCUMENT"
title = "document title"
text = f'{data}'
output_dimensionality = 256

# Load the model
model = TextEmbeddingModel.from_pretrained(MODEL_ID)

kwargs = (
    dict(output_dimensionality=output_dimensionality)
    if output_dimensionality
    else {}
)

# Create the input for the model
text_embedding_input = TextEmbeddingInput(
    task_type=task_type, title=title, text=text
)

# Get embeddings
embeddings = model.get_embeddings([text_embedding_input], **kwargs)

# Print the embeddings
for embedding in embeddings:
    vector = embedding.values
    print(vector)
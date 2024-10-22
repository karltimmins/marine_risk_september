# Marine Risk - Accenture

## Description
A project to improve risk assessment in marine traffic, using Genrative AI.

## Technologies
- Python
- List any other technologies, libraries, or tools used in the project, for example:
  - Streamlit
  - GCP
  - Vertex AI
  - Pandas
  - Venv

  - All dependencies are listed in the [requirements.txt](requirements.txt) file.

## Installation
Step-by-step instructions on how to set up the project locally.

1. Clone the repository:
    ```bash
    git clone https://github.com/karltimmins/marine_risk_september 
    ```

2. Install the dependencies

    ```python
    pip install -r requirements.txt
    ```

3. Set up virtual enviornment (optional) - venv

    ```python
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Set up GCP enviornment variables to connect to GCP.

5. To output embeddings for the 'training_data.json' file, run the script -

    ```python
    python3 embeddings_gcp_2.py 
    ```


5. To deploy a Streamlit frontend connected to a model run script -
    
    ```python
    python3 streamlit_gcp.py
    ```

5. To deploy a model which can respond to the 'training_data.json', run the script -
    
    ```python
    python3 vertex_api.py
    ```


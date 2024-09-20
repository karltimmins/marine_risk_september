from google.cloud import aiplatform
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')

load_dotenv(dotenv_path)

PROJECT_ID = os.environ.get("GCP_PROJECT")


def vector_search_create_index_endpoint(
    project=PROJECT_ID,
    location="us-central1",
    display_name="marine_risk"
) -> None:
    """Create a vector search index endpoint.

    Args:
        project (str): Required. Project ID
        location (str): Required. The region name
        display_name (str): Required. The index endpoint display name
    """
    # Initialize the Vertex AI client
    aiplatform.init(project=project, location=location)
    print(f"suceess")

    # Create Index Endpoint
    index_endpoint = aiplatform.MatchingEngineIndexEndpoint.create(
        display_name=display_name,
        public_endpoint_enabled=True,
        description="Matching Engine Index Endpoint",
    )

    print(f"Index Endpoint created successfully: {index_endpoint.resource_name}")


def vector_search_deploy_index(
    project="acn-uki-ds-data-ai-project",
    location="us-central1",
    index_name="marine_risk",
    index_endpoint_name="marine_risk_index_endpoint",
    deployed_index_id="1"
) -> None:
    """Deploy a vector search index to a vector search index endpoint.

    Args:
        project (str): Required. Project ID
        location (str): Required. The region name
        index_name (str): Required. The index to update. A fully-qualified index
          resource name or a index ID.  Example:
          "projects/123/locations/us-central1/indexes/my_index_id" or
          "my_index_id".
        index_endpoint_name (str): Required. Index endpoint to deploy the index to.
        deployed_index_id (str): Required. The user specified ID of the DeployedIndex.
    """
    # Initialize the Vertex AI client
    aiplatform.init(project=project, location=location)

    # Create the index instance from an existing index
    index = aiplatform.MatchingEngineIndex(index_name=index_name)

    # Create the index endpoint instance from an existing endpoint.
    index_endpoint = aiplatform.MatchingEngineIndexEndpoint(
        index_endpoint_name=index_endpoint_name
    )

    # Deploy Index to Endpoint
    index_endpoint = index_endpoint.deploy_index(
        index=index, deployed_index_id=deployed_index_id
    )

    print(index_endpoint.deployed_indexes)

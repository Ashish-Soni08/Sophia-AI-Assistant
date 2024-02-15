import logging
from langchain_community.llms import Clarifai
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_model_response(api_key: str, user_id: str, app_id: str, model_id: str, model_version_id: str, metadata: Dict[str, str], tags: List[str]) -> Dict:
    """
    Get model response from Clarifai API.
    
    Args:
        api_key (str): API key for Clarifai.
        user_id (str): User ID for Clarifai.
        app_id (str): App ID for Clarifai.
        model_id (str): Model ID for Clarifai.
        model_version_id (str): Model version ID for Clarifai.
        metadata (Dict[str, str]): Metadata for the request.
        tags (List[str]): Tags for the request.
        
    Returns:
        Dict: The response from the Clarifai API.
        
    Raises:
        ValueError: If any of the string inputs are not valid strings.
        Exception: If there's an error during the API call.
    """
    # Input validation
    string_inputs = [api_key, user_id, app_id, model_id, model_version_id]
    if not all(isinstance(item, str) and item.strip() for item in string_inputs):
        raise ValueError("All string inputs must be non-empty strings.")
    if not isinstance(metadata, Dict) or not isinstance(tags, List):
        raise ValueError("Metadata must be a dictionary and tags must be a list.")

    try:
        response = Clarifai(pat=api_key,
                            user_id=user_id,
                            app_id=app_id,
                            model_id=model_id,
                            model_version_id=model_version_id,
                            metadata=metadata,
                            tags=tags
                            )
        return response
    except Exception as e:
        logging.error(f"An error occurred during the API call to Clarifai: {e}")
        raise e
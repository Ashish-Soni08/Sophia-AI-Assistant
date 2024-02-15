from constants import CLARIFAI_API_KEY
from inference import generate_model_response

# Credentials for accessing GPT-4 Vision on Clarifai
USER_ID: str = 'openai'
APP_ID: str = 'chat-completion'
MODEL_ID: str = 'openai-gpt-4-vision'
MODEL_VERSION_ID: str = '266df29bc09843e0aee9b7bf723c03c2'

# GPT-4 Vision
gpt4_vision_llm = generate_model_response(api_key=CLARIFAI_API_KEY,
                                         user_id=USER_ID,
                                         app_id=APP_ID,
                                         model_id=MODEL_ID,
                                         model_version_id=MODEL_VERSION_ID,
                                         metadata={'app_id': APP_ID, 
                                                    'model_name': MODEL_ID,
                                                    'model_version': MODEL_VERSION_ID,
                                                    'model_provider': USER_ID},
                                         tags=['research_agent', 'openai'])
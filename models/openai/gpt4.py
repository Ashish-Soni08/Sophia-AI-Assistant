from constants import CLARIFAI_API_KEY
from inference import generate_model_response

# Credentials for accessing GPT-4 on Clarifai
USER_ID: str = 'openai'
APP_ID: str = 'chat-completion'
MODEL_ID: str = 'GPT-4'
MODEL_VERSION_ID: str = '5d7a50b44aec4a01a9c492c5a5fcf387'

# GPT-4
gpt4_llm = generate_model_response(api_key=CLARIFAI_API_KEY,
                                   user_id=USER_ID,
                                   app_id=APP_ID,
                                   model_id=MODEL_ID,
                                   model_version_id=MODEL_VERSION_ID,
                                   metadata={'app_id': APP_ID, 
                                            'model_name': MODEL_ID,
                                            'model_version': MODEL_VERSION_ID,
                                            'model_provider': USER_ID},
                                   tags=['text_generation', 'openai'])
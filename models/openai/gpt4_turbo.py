from constants import CLARIFAI_API_KEY
from inference import generate_model_response

# Credentials for accessing GPT-4 Turbo on Clarifai
USER_ID: str = 'openai'
APP_ID: str = 'chat-completion'
MODEL_ID: str = 'gpt-4-turbo'
MODEL_VERSION_ID: str = '182136408b4b4002a920fd500839f2c8'

# GPT-4 Turbo
gpt4_turbo_llm = generate_model_response(api_key=CLARIFAI_API_KEY,
                                         user_id=USER_ID,
                                         app_id=APP_ID,
                                         model_id=MODEL_ID,
                                         model_version_id=MODEL_VERSION_ID,
                                         metadata={'app_id': APP_ID, 
                                                'model_name': MODEL_ID,
                                                'model_version': MODEL_VERSION_ID,
                                                'model_provider': USER_ID},
                                         tags=['text_generation', 'openai'])
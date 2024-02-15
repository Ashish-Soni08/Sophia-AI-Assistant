from constants import OPENAI_API_KEY
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)

# Image API
def generate_image(prompt: str, model_name: str = "dall-e-3", n: int = 1, size: str = "1024x1024", response_format = "url", quality: str = "standard"):
    generation_response = client.images.generate(model = model_name,
                                                 prompt=prompt,
                                                 n=n,
                                                 size=size,
                                                 response_format=response_format,
                                                 quality=quality)
    return generation_response

# Text to Speech API
def text_to_speech(input_text: str, model_name: str = "tts-1-hd", voice: str = "nova"):
    response = client.audio.speech.create(model=model_name, 
                                          voice=voice, 
                                          input=input_text)
    return response
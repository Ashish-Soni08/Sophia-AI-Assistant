from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

# API KEYS, URLS, TOKENS, ETC

## Model Providers

# Anthropic
ANTHROPIC_API_KEY: str = config["ANTHROPIC_API"]


# Clarifai
CLARIFAI_API_KEY: str = config["CLARIFAI_API"]

# Hugging Face
HUGGINGFACE_API_KEY: str = config["HF_API"] # Read
HF_TOKEN: str = config["HF_TOKEN"] # Write

######################

## LangChain
LANGCHAIN_API_KEY: str = config["LANGCHAIN_API"]
LANGCHAIN_URL: str = config["LANGCHAIN_ENDPOINT"]
LANGCHAIN_PROJECT: str = config["LANGCHAIN_PROJECT"]

## JINA AI
BESTBANNER_API_KEY: str = config["BESTBANNER_API"]
JINA_API_KEY: str = config["JINACHAT_API"]
PROMPTPERFECT_API_KEY: str = config["PROMPTPERFECT_API"]
RATIONALE_API_KEY: str = config["RATIONALE_API"]
SCENEXPLAIN_API_KEY: str = config["SCENEXPLAIN_API"]

## OpenAI
OPENAI_API_KEY: str = config["OPENAI_API"]

## Pinecone
PINECONE_API_KEY: str = config["PINECONE_API"]

## Super AGI
SUPERAGI_API_KEY: str = config["SUPERAGI_API"]
import weaviate
from app.configs.app_configs import settings
from dotenv import load_dotenv
import os

load_dotenv()

def weaviate_connection():
    client = weaviate.Client(
        url = 'https://5esjfd57suivc9j0xkf4tg.c0.us-west3.gcp.weaviate.cloud',
        auth_client_secret=weaviate.auth.AuthApiKey(api_key='klxlV8pCDJazHg7VXCa4QjPz3e868Ad6RyZI'),
        additional_headers = {
            "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
        }
    )
    return client



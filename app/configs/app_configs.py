from dotenv import load_dotenv
import os

load_dotenv()

class Settings():
    wsc_url: str = os.getenv("WCS_URL")
    wsc_api_key: str = os.getenv("WCS_API_KEY")
    openai_api_key:  str = os.getenv("OPENAI_API_KEY")
    collection_name: str = os.getenv("COLLECTION_NAME")
    firecrawl_api_key: str = os.getenv("FIRECRAWL_API_KEY")

settings = Settings()



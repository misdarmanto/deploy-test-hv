from app.configs.app_configs import app_configs
from app.configs.weaviate_connection import weaviate_connection
import weaviate.classes as wvc

def create_collection():
    client = weaviate_connection()
    colection = client.collections.create(
            name=app_configs['weaviate_collection_name'],
            vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai(),  
            generative_config=wvc.config.Configure.Generative.openai() 
        )
    return colection
from langchain.vectorstores.weaviate import Weaviate
from langchain.llms import OpenAI
from langchain.chains import ChatVectorDBChain
from app.configs.weaviate_connection import weaviate_connection
from app.models.schemas import QueryIndexingModel
from app.configs.app_configs import settings
from fastapi import APIRouter

app = APIRouter(
    prefix="/indexing",
    tags=["indexing"]
)

@app.get("/")
def query_object(request_body: QueryIndexingModel):
    try:
        client = weaviate_connection()
        data = Weaviate(client,"Haven", "answer")
        MyOpenAI = OpenAI(temperature=0.2, openai_api_key=settings.openai_api_key)
        question = ChatVectorDBChain.from_llm(MyOpenAI, data)

        chat_history = []

        result = question({"question": request_body.question, "chat_history": chat_history})
        chat_history = [(request_body.question, result["answer"])]
        return {"message" : result["answer"]}            
    except Exception as e:
        return {"error": str(e)}




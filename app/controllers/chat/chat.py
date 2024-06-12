from langchain.vectorstores.weaviate import Weaviate
from fastapi import APIRouter, Request
from langchain.llms import OpenAI
from langchain.chains import ChatVectorDBChain
from app.configs.weaviate_connection import weaviate_connection
from app.configs.app_configs import settings
import requests

app = APIRouter(
    prefix="/chats",
    tags=["chats"]
)

SENDIRD_APP_ID = '33FB955C-246A-404F-A6A2-FCB7646D240E'
SENDIRD_API_TOKEN = '459dba06b6cc6c1be5760fcc630796fa28c21e7e'
# CHANNEL_URL = 'sendbird_open_channel_20093_3943bc013c52c15b23917a01286d24c1e46830db'

def send_message_to_channel(channel_url: str, message: str):
    url = f'https://api-{SENDIRD_APP_ID}.sendbird.com/v3/group_channels/{channel_url}/messages'
    headers = {
        'Api-Token': SENDIRD_API_TOKEN,
        'Content-Type': 'application/json'
    }
    data = {
        'message_type': 'MESG',
        'user_id': 'marissa',  
        'message': message
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(response.json())
    print(f'send data  {data}')
    return response.json()

@app.get("/")
def chat(query: str):
    try:
        client = weaviate_connection()
        data = Weaviate(client,"Haven", "text")
        MyOpenAI = OpenAI(temperature=0.2, openai_api_key=settings.openai_api_key)
        question = ChatVectorDBChain.from_llm(MyOpenAI, data)

        chat_history = []
 
        result = question({"question": query, "chat_history": chat_history})
        chat_history = [(query, result["answer"])]
        return {"message" : result["answer"]}
    except Exception as e:
        return {"error": str(e)}
    

@app.post("/webhook")
async def webhook(request: Request):
    print("call")
    try:
        data = await request.json()
        event_type = data.get('category')
        channel_url = data['channel']['channel_url']
        sender = data.get("sender", None)
        
        if sender != None:
            if sender["user_id"] == "marissa":
                return ""

        if event_type == 'group_channel:message_send':
            received_message = data['payload']['message']

            client = weaviate_connection()
            data = Weaviate(client,"Haven", "text")
            MyOpenAI = OpenAI(temperature=0.2, openai_api_key=settings.openai_api_key)
            question = ChatVectorDBChain.from_llm(MyOpenAI, data)

            query = received_message

            chat_history = []

            result = question({"question": query, "chat_history": chat_history})
            chat_history = [(query, result["answer"])]
            send_message_to_channel(channel_url, result["answer"])
        
    except Exception as e:
        print(e)
        return {"error": str(e)}

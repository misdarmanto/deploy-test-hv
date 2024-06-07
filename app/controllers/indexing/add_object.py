from app.configs.weaviate_connection import weaviate_connection
from app.models.schemas import AddObectWeaviate
from typing import List
from fastapi import APIRouter

app = APIRouter(
    prefix="/indexing",
    tags=["indexing"]
)

@app.post("/")
def add_obejct(request_body: List[AddObectWeaviate]):
    client = weaviate_connection()
    try:
        client.batch.configure(batch_size=100)
        for data in request_body:
            client.batch.add_data_object(
                data_object=dict(data),
                class_name="Haven"
            )
        return {"message" : f'data imported {len(request_body)}'}
    except Exception as e:
        return {"error": str(e)}
 

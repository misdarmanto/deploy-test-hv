from pydantic import BaseModel
from uuid import UUID

class WeaviateObjectBase(BaseModel):
    text: str
    link: str
    object_id: str 

class WeaviateObjectCreate(WeaviateObjectBase):
    collection_id: UUID

class WeaviateObject(WeaviateObjectBase):
    id: UUID

    class Config:
        orm_mode = True

class WeaviateCollectionBase(BaseModel):
    collection_name: str

class WeaviateCollectionCreate(WeaviateCollectionBase):
    pass

class WeaviateCollection(WeaviateCollectionBase):
    id: UUID
    objects: list[WeaviateObject] = []

    class Config:
        orm_mode = True

class GetObectWeaviate(BaseModel):
    question: str

class AddObectWeaviate(BaseModel):
    question: str
    answer: str
    category: str

class QueryIndexingModel(BaseModel):
    question: str

class ScrapingModel(BaseModel):
    url: str

class UploadXlsxFileRequest(BaseModel):
    collection_name: str
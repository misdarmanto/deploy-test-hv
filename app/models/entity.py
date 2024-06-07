from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.configs.settings import Base

class WeaviateCollection(Base):
    __tablename__ = "weaviate_collection"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    collection_name = Column(String, unique=True, index=True)
    objects = relationship("WeaviateObject", back_populates="collection")

class WeaviateObject(Base):
    __tablename__ = "weaviate_object"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    text = Column(Text)
    link = Column(Text)
    object_id = Column(String)
    collection_id = Column(UUID(as_uuid=True), ForeignKey("weaviate_collection.id"))
    collection = relationship("WeaviateCollection", back_populates="objects")

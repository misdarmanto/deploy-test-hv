from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.models import entity, schemas
from app.configs.settings import get_db

app = APIRouter(
    prefix="/collections",
    tags=["collections"]
)

@app.post("/", response_model=schemas.WeaviateCollection)
def create_collection(collection: schemas.WeaviateCollectionCreate, db: Session = Depends(get_db)):
    db_collection = get_collection_by_name(db, collection_name=collection.collection_name)
    if db_collection:
        raise HTTPException(status_code=400, detail="Collection name already registered")
    return create_collection(db=db, collection=collection)

@app.get("/{collection_id}", response_model=schemas.WeaviateCollection)
def read_collection(collection_id: UUID, db: Session = Depends(get_db)):
    db_collection = get_collection(db, collection_id=collection_id)
    if db_collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    return db_collection

@app.get("/", response_model=list[schemas.WeaviateCollection])
def read_collections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    collections = get_collections(db, skip=skip, limit=limit)
    return collections

@app.delete("/{collection_id}", response_model=schemas.WeaviateCollection)
def delete_collection(collection_id: UUID, db: Session = Depends(get_db)):
    db_collection = get_collection(db, collection_id=collection_id)
    if db_collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    return delete_collection(db=db, collection_id=collection_id)


# Collection CRUD
def get_collection(db: Session, collection_id: UUID):
    return db.query(entity.WeaviateCollection).filter(entity.WeaviateCollection.id == collection_id).first()

def get_collection_by_name(db: Session, collection_name: str):
    return db.query(entity.WeaviateCollection).filter(entity.WeaviateCollection.collection_name == collection_name).first()

def get_collections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(entity.WeaviateCollection).offset(skip).limit(limit).all()

def create_collection(db: Session, collection: schemas.WeaviateCollectionCreate):
    db_collection = entity.WeaviateCollection(collection_name=collection.collection_name)
    db.add(db_collection)
    db.commit()
    db.refresh(db_collection)
    return db_collection

def delete_collection(db: Session, collection_id: UUID):
    db_collection = db.query(entity.WeaviateCollection).filter(entity.WeaviateCollection.id == collection_id).first()
    if db_collection:
        db.delete(db_collection)
        db.commit()
    return db_collection

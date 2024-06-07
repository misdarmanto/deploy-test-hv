from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.models import entity, schemas
from app.configs.settings import get_db

app = APIRouter(
    prefix="/objects",
    tags=["objects"]
)

@app.post("/", response_model=schemas.WeaviateObject)
def create_object(obj: schemas.WeaviateObjectCreate, db: Session = Depends(get_db)):
    return create_object(db=db, obj=obj)

@app.get("/{object_id}", response_model=schemas.WeaviateObject)
def read_object(object_id: UUID, db: Session = Depends(get_db)):
    db_object = get_object(db, object_id=object_id)
    if db_object is None:
        raise HTTPException(status_code=404, detail="Object not found")
    return db_object

@app.get("/", response_model=list[schemas.WeaviateObject])
def read_objects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    objects = get_objects(db, skip=skip, limit=limit)
    return objects

@app.delete("/{object_id}", response_model=schemas.WeaviateObject)
def delete_object(object_id: UUID, db: Session = Depends(get_db)):
    db_object = get_object(db, object_id=object_id)
    if db_object is None:
        raise HTTPException(status_code=404, detail="Object not found")
    return delete_object(db=db, object_id=object_id)


# Object CRUD
def get_object(db: Session, object_id: UUID):
    return db.query(entity.WeaviateObject).filter(entity.WeaviateObject.id == object_id).first()

def get_objects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(entity.WeaviateObject).offset(skip).limit(limit).all()

def create_object(db: Session, obj: schemas.WeaviateObjectCreate):
    print("save backup data to data base")
    db_object = entity.WeaviateObject(
        text=obj.text,
        link=obj.link,
        object_id=obj.object_id,
        collection_id=obj.collection_id
    )
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object

def delete_object(db: Session, object_id: UUID):
    db_object = db.query(entity.WeaviateObject).filter(entity.WeaviateObject.id == object_id).first()
    if db_object:
        db.delete(db_object)
        db.commit()
    return db_object

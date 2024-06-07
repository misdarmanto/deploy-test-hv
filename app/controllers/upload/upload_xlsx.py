import io
import pandas as pd
from app.controllers.scraping.scraping import web_scraping
from app.controllers.indexing.add_object import add_obejct
from app.models.schemas import ScrapingModel, WeaviateObjectCreate
from fastapi import APIRouter,File, UploadFile, Query, Depends
from app.controllers.backup import weaviate_object
from app.configs.settings import get_db
from sqlalchemy.orm import Session

app = APIRouter(
    prefix="/uploads",
    tags=["uploads"]
)

@app.post("/upload/xlsx")
def extract_text_from_xlsx(file : UploadFile = File(...), db: Session = Depends(get_db), collection_id: str = Query(...)):
    try:
        content = file.file.read()
        df = pd.read_excel(io.BytesIO(content).getvalue())
        for url in df["url"]:
            scraping_instance = ScrapingModel(url=url)
            docs = web_scraping(scraping_instance)

            filtered_docs = []

            if(len(docs) > 0):
                for doc in docs:
                    question = doc.metadata["title"]
                    answer =  doc.page_content
                    filtered_docs.append({"question" : question ,"answer": answer})

                    backup_data = WeaviateObjectCreate(
                        text=doc.page_content,
                        link=url,
                        collection_id=collection_id,
                        object_id= "Sdsd"
                    )
                    
                    weaviate_object.create_object(db=db, obj=backup_data)
                add_obejct(filtered_docs) 
                return filtered_docs
    except Exception as e:
        return {"error": str(e)}
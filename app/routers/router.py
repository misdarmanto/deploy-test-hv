from fastapi.routing import APIRouter
# from app.controllers.backup import weaviate_collections, weaviate_object
from app.controllers.chat import chat
# from app.controllers.upload import upload_pdf, upload_xlsx
# from app.controllers.scraping import scraping
# from app.controllers.indexing import add_object, query_object
from app.controllers import main


api_router = APIRouter()

api_router.include_router(main.app)
# api_router.include_router(weaviate_collections.app)
# api_router.include_router(weaviate_object.app)
api_router.include_router(chat.app)
# api_router.include_router(upload_pdf.app)
# api_router.include_router(upload_xlsx.app)
# api_router.include_router(scraping.app)
# api_router.include_router(query_object.app)
# api_router.include_router(add_object.app)
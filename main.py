from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import entity
from app.configs.settings import engine
from app.routers.router import api_router

entity.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(router=api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

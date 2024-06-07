from app.models.schemas import ScrapingModel
from langchain_community.document_loaders import FireCrawlLoader
from fastapi import APIRouter

app = APIRouter(
    prefix="/scraping",
    tags=["scraping"]
)

@app.post("/")
def web_scraping(request_body: ScrapingModel):
    try:
        loader = FireCrawlLoader(
            api_key="fc-d888b7d5440149e2ae010ca1fb665f89", url=request_body.url, mode="scrape",
        )

        docs = loader.load()
        return docs
    except Exception as e:
        return {"error": str(e)}
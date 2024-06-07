import io
import PyPDF2
from fastapi import APIRouter,File, UploadFile

app = APIRouter(
    prefix="/uploads",
    tags=["uploads"]
)

@app.post("/upload/pdf")
def extract_text_from_pdf(file: UploadFile = File(...)):
    try:
        text = ""
        content = file.file.read()
        pdf_file = io.BytesIO(content)
        reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text
    except Exception as e:
        return {"error": str(e)}

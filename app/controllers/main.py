from fastapi import APIRouter

app = APIRouter()

@app.get("/")
def main():
    return {"message" : "welcome to haven api"}


from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(root_path="/Prod")

@app.get("/")
def root():
    return {"message": "Hello from Lambda"}

handler = Mangum(app)

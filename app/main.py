from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Lambda Function URL"}

handler = Mangum(app)

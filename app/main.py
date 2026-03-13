from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Root!!!"}

@app.get("/hello")
def new():
    return {"message": "Hello!!!"}

@app.get("/bye")
def bye():
    return {"message": "Bye!!!"}

handler = Mangum(app)

from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Lambda Function URL"}

@app.get("/new")
def new():
    return {"message": "New Endpoint added in Lambda Function URL"}

@app.get("/hello")
def new():
    return {"message": "Hello from new lambda instance"}

@app.get("/bye")
def bye():
    return {"message": "Bye!!!"}

handler = Mangum(app)

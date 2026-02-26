import os, boto3
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
db = boto3.resource("dynamodb").Table(os.environ['TABLE_NAME'])

@app.get("/images")
def list_images():
    return {"images": db.scan().get("Items", [])}

handler = Mangum(app)

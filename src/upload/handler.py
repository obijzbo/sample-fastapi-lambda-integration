import os, uuid, boto3
from fastapi import FastAPI, UploadFile, File
from mangum import Mangum

app = FastAPI()
s3 = boto3.client("s3")
db = boto3.resource("dynamodb").Table(os.environ['TABLE_NAME'])

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    s3_key = f"{file_id}-{file.filename}"
    s3.upload_fileobj(file.file, os.environ['BUCKET_NAME'], s3_key)
    
    url = f"https://{os.environ['BUCKET_NAME']}.s3.amazonaws.com/{s3_key}"
    db.put_item(Item={'file_id': file_id, 'url': url, 'name': file.filename})
    return {"status": "uploaded", "url": url}

handler = Mangum(app)

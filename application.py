from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
import boto3
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

application = FastAPI()

@application.get('/helo')
def index():
    return 200, "Hello World"
    
@application.get('/')
def index():
    return 200, "Hello World"

@application.post("/upload_image")
async def upload_image(file: UploadFile = File(...)):
    bucket_name = os.environ['BUCKET_NAME']

    try:
        
        return JSONResponse(status_code=201, content={"message": "Image uploaded successfully"})
    except Exception as e:
        print(f"Error uploading image: {e}")
        raise HTTPException(status_code=400, detail="Error uploading image")

if __name__ == "__main__":
    application.debug = True
    application.run()

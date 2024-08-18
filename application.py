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


if __name__ == "__main__":
    application.debug = True
    application.run()

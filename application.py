from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
import boto3
import os
import uvicorn


application = FastAPI()


@application.get('/')
def index():
    return 200, "Hello World"

if __name__ == "__main__":
    uvicorn.run(application, port=5000)

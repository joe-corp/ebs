from fastapi import FastAPI
application = FastAPI()
@application.get('/')
def index():
    """Main Page"""
    return "Hello World New"

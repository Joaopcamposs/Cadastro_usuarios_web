# Import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import api

# Initialize the app
app = FastAPI()

app.include_router(api.router)

#uvicorn --reload main:app

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to WEB users sign"}

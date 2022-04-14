from fastapi import FastAPI
from backend.app import api

app = FastAPI()

# include routes from api
app.include_router(api.app)


# run application
# uvicorn --reload backend.app.main:app

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to WEB users sign"}

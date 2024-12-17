from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/pwd")
def pwd():
    path = os.getcwd()
    print(f'path={path}')
    return path

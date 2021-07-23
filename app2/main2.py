from starlette.responses import Response
import uvicorn
import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/cont1/")
def read_cont1():
    resp = requests.get('http://cont1:8080/')
    return {"message":resp.text, "code":resp.status_code}

@app.get("/cont1/{name}")
def read_cont1_2(name):
    resp = requests.get('http://cont1:8080/{}'.format(name))
    return {"message":resp.text, "code":resp.status_code}

@app.get("/")
def read_root():
    return "{Hello hanish}"
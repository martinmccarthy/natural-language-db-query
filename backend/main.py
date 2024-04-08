import os

from fastapi import FastAPI
import google.generativeai as genai

app = FastAPI()


@app.get("/")
def hello():
    genai.configure(api_key=os.environ["API_KEY"])
    response = genai.chat(messages="Hello")
    return response.last

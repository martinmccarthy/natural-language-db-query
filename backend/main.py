import os

from fastapi import FastAPI
import google.generativeai as genai

app = FastAPI()

@app.get("/")
def hello():
    print(os.environ["API_KEY"])
    genai.configure(api_key=os.environ["API_KEY"])
    response = genai.chat(messages="Hello")
    return response.last

@app.get("/chat")
def chat(message: str, prompt:str):
    genai.configure(api_key=os.environ["API_KEY"])
    response = genai.chat(messages=message, context=prompt)
    return response.last
from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def display():
        return{
            "message": "Hello World"
        }
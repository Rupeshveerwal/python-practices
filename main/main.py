from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def display():{
        "message" : "Hello Kashish"
    }















# @api.get("/add")
# def add(a:int,b:int):
#     c = a + b   
#     return {
#         "result": c 
#     }
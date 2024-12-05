from fastapi import FastAPI

app = FastAPI()


@app.get("/service1/")
async def root():
    return "Hello World, this is server 1"


@app.get("/service1/be1", status_code=200)
async def be1():
    return "Hello World, this is server 1"

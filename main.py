from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World, this is server 1"}


@app.get("/be1", status_code=200)
async def be1():
    return {"message": "Hello World, this is server 1"}

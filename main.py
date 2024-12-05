from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    return "Hello World, this is server 1"

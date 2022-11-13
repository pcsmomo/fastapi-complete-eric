from fastapi import FastAPI

app = FastAPI()

BOOKS = []


@app.get("/")
async def read_all_books():
    return BOOKS

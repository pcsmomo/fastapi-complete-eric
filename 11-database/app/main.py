from fastapi import FastAPI
import app.models as models
from app.database import engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def create_database():
    return {"Database": "Created"}

from fastapi import FastAPI, Depends
import app.models as models
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def read_all(db: Session = Depends(get_db)):
    # return {"Database": "Created"}
    return db.query(models.Todos).all()

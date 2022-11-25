from fastapi import FastAPI

import app.models as models
from app.database import engine
from app.routers import auth, todos
from app.company import companyapis

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(
    companyapis.router,
    prefix="/compnayapis",
    tags=["companyapis"],
    responses={418: {"description": "Internal Use Only"}}
)

from fastapi import FastAPI
import app.models as models
from app.database import engine
from app.routers import auth, todos, admin

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)

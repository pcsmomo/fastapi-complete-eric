from fastapi import FastAPI, Depends

import app.models as models
from app.database import engine
from app.routers import auth, todos, users

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
# app.include_router(
#     companyapis.router,
#     prefix="/compnayapis",
#     tags=["companyapis"],
#     dependencies=[Depends(dependencies.get_token_header)],
#     responses={418: {"description": "Internal Use Only"}}
# )

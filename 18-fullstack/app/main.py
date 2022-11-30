from fastapi import FastAPI, Depends

import app.models as models
from app.database import engine
from app.routers import auth, todos, users
from starlette.staticfiles import StaticFiles
from starlette import status
from starlette.responses import RedirectResponse

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def root():
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)

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

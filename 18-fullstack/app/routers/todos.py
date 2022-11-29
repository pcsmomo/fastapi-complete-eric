from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Optional
from fastapi import Depends, HTTPException, APIRouter, Request, Form
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

from starlette import status
from starlette.responses import RedirectResponse

import app.models as models
from app.database import engine, SessionLocal
from .auth import get_current_user, get_user_exception

import sys
sys.path.append("..")


router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="app/templates")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/", response_class=HTMLResponse)
async def read_all_by_user(request: Request, db: Session = Depends(get_db)):

    todos = db.query(models.Todos).filter(models.Todos.owner_id == 1).all()

    return templates.TemplateResponse("home.html", {"request": request, "todos": todos})


@router.get("/add-todo", response_class=HTMLResponse)
async def add_new_todo(request: Request):
    return templates.TemplateResponse("add-todo.html", {"request": request})


@router.post("/add-todo", response_class=HTMLResponse)
async def create_todo(request: Request, title: str = Form(), description: str = Form(),
                      priority: int = Form(), db: Session = Depends(get_db)):
    todo_model = models.Todos()
    todo_model.title = title
    todo_model.description = description
    todo_model.priority = priority
    todo_model.complete = False
    todo_model.owner_id = 1

    db.add(todo_model)
    db.commit()

    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


@router.get("/edit-todo/{todo_id}", response_class=HTMLResponse)
async def add_new_todo(request: Request):
    return templates.TemplateResponse("edit-todo.html", {"request": request})

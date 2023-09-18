from typing import Annotated, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

from app.models import Todos
from app.database import engine, SessionLocal
from .auth import get_current_user


router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


class TodoRequest(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description="The priority must be between 1-5")
    complete: bool


@router.get("/")
async def read_all(db: db_dependency):
    # return {"Database": "Created"}
    return db.query(Todos).all()


@router.get("/todo/{todo_id}")
async def read_todo(todo_id: int, db: db_dependency):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    print(todo_model)
    if todo_model is not None:
        return todo_model
    raise http_exception()


@router.post("/")
async def create_todo(
    user: user_dependency, todo_request: TodoRequest, db: db_dependency
):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    todo_model = Todos(**todo_request.model_dump(), owner_id=user.get("id"))
    # old way
    # todo_model = Todos()
    # todo_model.title = todo.title
    # todo_model.description = todo.description
    # todo_model.priority = todo.priority
    # todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return successful_response(201)


@router.put("/{todo_id}")
async def update_todo(todo_id: int, todo: TodoRequest, db: db_dependency):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise http_exception()

    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return successful_response(200)


@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, db: db_dependency):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise http_exception()

    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()

    return successful_response(200)


def successful_response(status_code: int):
    return {"status": status_code, "transaction": "Successful"}


def http_exception():
    return HTTPException(status_code=404, detail="Todo not found")

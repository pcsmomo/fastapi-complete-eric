from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import app.models as models


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str


app = FastAPI()


@app.post("/create/user")
async def create_new_user(create_user: CreateUser):
    create_user_model = models.Users()
    create_user_model.email = create_user.email
    create_user_model.username = create_user.username
    create_user_model.first_name = create_user.email
    create_user_model.last_name = create_user.last_name
    create_user_model.hashed_password = create_user.password
    create_user_model.is_active = True

    return create_user_model

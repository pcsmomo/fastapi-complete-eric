from typing import Optional
from fastapi import Depends, APIRouter
import app.models as models
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user, get_user_exception

import sys
sys.path.append("..")

router = APIRouter(
    prefix="/address",
    tags=["address"],
    responses={404: {"description": "Not found"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Address(BaseModel):
    address1 = str
    address2 = Optional[str]
    city = str
    state = str
    country = str
    postalcode = str

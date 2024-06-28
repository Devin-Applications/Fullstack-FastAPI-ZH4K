from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    hashed_password: str

class UserUpdate(UserBase):
    hashed_password: Optional[str] = None

class User(UserBase):
    id: uuid.UUID

    class Config:
        orm_mode: True

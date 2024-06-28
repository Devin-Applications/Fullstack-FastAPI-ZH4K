from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid
from passlib.context import CryptContext

from app.dependencies import get_sync_db
from app.schemas import User, UserCreate, UserUpdate
from app.crud import user_crud

router = APIRouter()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_sync_db)):
    db_user = user_crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    # Hash the password before creating the user
    hashed_password = pwd_context.hash(user.password)
    user_data = user.dict()
    user_data['hashed_password'] = hashed_password
    return user_crud.create_user(db=db, user=UserCreate(**user_data))

@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_sync_db)):
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: uuid.UUID, db: Session = Depends(get_sync_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: uuid.UUID, user: UserUpdate, db: Session = Depends(get_sync_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_crud.update_user(db=db, user_id=user_id, user=user)

@router.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: uuid.UUID, db: Session = Depends(get_sync_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_crud.delete_user(db=db, user_id=user_id)

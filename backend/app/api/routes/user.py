from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import User
from app.schemas.user import  UserCreate
from app.schemas.user import UserResponse
from app.schemas.user import UserUpdate
from app.core.exceptions import AppException

router = APIRouter()

# here we are inserting the data into database
@router.post("/users")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    
    new_user = User(
        username = user.username,
        email = user.email
    )
    
    db.add(new_user)
    
    db.commit()
    
    db.refresh(new_user)
    
    return new_user

# here we retrive data from database
@router.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    
    users = db.query(User).all()
    
    return users


# here we are updating record in database
@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    
    db_user = db.query(User).filter(User.id == user_id).first()
    
    if not db_user:
        raise AppException("user not found...", 400)
    
    db_user.username = user.username
    db_user.email = user.email
    
    db.commit()
    
    db.refresh(db_user)
    
    return db_user


# here we are deleting record from database
@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise AppException("user not found...", 400)
    
    db.delete(user)
    
    db.commit()
    
    return {
        "message": "User deleted successfully."
    }

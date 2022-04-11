from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import get_all_users, create_user, get_user_by_id, update_user, delete_user
from database import get_db
from exceptions import UserException
from schemas import User, CreateAndUpdateUser
import sys

sys.setrecursionlimit(1500)
router = APIRouter()

# API to get the list of users
@router.get("/users")
def list_users(session: Session = Depends(get_db)):
    users_list = get_all_users(session=session)

    return users_list


# API endpoint to add a user to the database
@router.post("/user")
def add_user(new_user: CreateAndUpdateUser, session: Session = Depends(get_db)):
    try:
        user = create_user(session, new_user)
        return user
    except UserException as cie:
        raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular user
@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, session: Session = Depends(get_db)):
    try:
        user = get_user_by_id(session, user_id)
        return user
    except UserException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing user
@router.put("/users/{user_id}", response_model=User)
def update_user_info(user_id: int, new_info: CreateAndUpdateUser,
                session: Session = Depends(get_db)):
    try:
        user = update_user(session, user_id, new_info)
        return user
    except UserException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a user from the data base
@router.delete("/users/{user_id}")
def delete_user_info(user_id: int, session: Session = Depends(get_db)):
    try:
        return delete_user(session, user_id)
    except UserException as cie:
        raise HTTPException(**cie.__dict__)

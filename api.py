from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import get_all_users, create_user, update_user, delete_user, get_user_by_cpf
from database import get_db
from exceptions import UserException
from schemas import User, CreateAndUpdateUser

router = APIRouter()

# API to get the list of users
@router.get("/api/users")
def list_users(session: Session = Depends(get_db)):
    users_list = get_all_users(session=session)

    return users_list


# API endpoint to add a user to the database
@router.post("/api/user")
def add_user(new_user: CreateAndUpdateUser, session: Session = Depends(get_db)):
    try:
        user = create_user(session, new_user)
        return user
    except UserException as cie:
        raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular user by cpf
@router.get("/api/user/{user_cpf}", response_model=User)
def get_user_info(user_cpf: str, session: Session = Depends(get_db)):
    try:
        user = get_user_by_cpf(session, user_cpf)
        return user
    except UserException as cie:
        raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular user by id
# @router.get("/api/user/id&{user_id}", response_model=User)
# def get_user_id(user_id: int, session: Session = Depends(get_db)):
#     try:
#         user = get_user_by_id(session, user_id)
#         return user
#     except UserException as cie:
#         raise HTTPException(**cie.__dict__)


# API endpoint to update a existing user
@router.put("/api/user/{user_cpf}", response_model=User)
def update_user_info(user_cpf: str, new_info: CreateAndUpdateUser,
                session: Session = Depends(get_db)):
    try:
        user = update_user(session, user_cpf, new_info)
        return user
    except UserException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a user from the data base
@router.delete("/api/user/{user_cpf}")
def delete_user_info(user_cpf: str, session: Session = Depends(get_db)):
    try:
        return delete_user(session, user_cpf)
    except UserException as cie:
        raise HTTPException(**cie.__dict__)

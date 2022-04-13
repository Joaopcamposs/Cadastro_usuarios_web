from fastapi import APIRouter, Depends, HTTPException, security
from sqlalchemy.orm import Session
from crud import get_all_users, create_user, update_user, delete_user, get_user_by_cpf
from database import get_db
from exceptions import UserException
from schemas import User, CreateAndUpdateUser
from services import authenticate_user_cpf, create_token, get_current_user

app = APIRouter()

# API endpoint to get the list of users
@app.get("/api/users")
async def list_users(session: Session = Depends(get_db)):
    users_list = await get_all_users(session=session)

    return users_list


# API endpoint to add a user to the database
@app.post("/api/user")
async def add_user(new_user: CreateAndUpdateUser, session: Session = Depends(get_db)):
    try:
        user = await create_user(session, new_user)
        return user
    except UserException as cie:
        raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular user by cpf
@app.get("/api/user/{user_cpf}", response_model=User)
async def get_user_info(user_cpf: str, session: Session = Depends(get_db)):
    try:
        user = await get_user_by_cpf(session, user_cpf)
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
@app.put("/api/user/{user_cpf}", response_model=User)
async def update_user_info(user_cpf: str, new_info: CreateAndUpdateUser,
                session: Session = Depends(get_db)):
    try:
        user = await update_user(session, user_cpf, new_info)
        return user
    except UserException as cie:
        raise HTTPException(**cie.__dict__)


# API endpoint to delete a user from the data base
@app.delete("/api/user/{user_cpf}")
async def delete_user_info(user_cpf: str, session: Session = Depends(get_db)):
    try:
        return await delete_user(session, user_cpf)
    except UserException as cie:
        raise HTTPException(**cie.__dict__)


# API endpoint to generate token
@app.post("/api/token")
async def generate_token(
        form_data: security.OAuth2PasswordRequestForm = Depends(),
        session: Session = Depends(get_db)
):
    user = await authenticate_user_cpf(session, form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    return await create_token(user)


# API endpoint to get current legged user
@app.get("/api/users/me", response_model=User)
async def get_user(user: User = Depends(get_current_user)):
    return user

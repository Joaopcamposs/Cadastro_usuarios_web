from typing import List
from sqlalchemy.orm import Session
from exceptions import UserAlreadyExistError, UserNotFoundError
from models import User
from schemas import CreateAndUpdateUser
import passlib.hash as hash


# Function to get list of users
def get_all_users(session: Session) -> List[User]:
    return session.query(User).all()


# Function to  get info of a particular user by id
# def get_user_by_id(session: Session, _id: int) -> User:
#     user = session.query(User).get(_id)
#
#     if user is None:
#         raise UserNotFoundError
#
#     return user


# Function to  get info of a particular user by CPF
def get_user_by_cpf(session: Session, _cpf: str) -> User:
    user = session.query(User).filter(User.CPF == _cpf).first()

    if user is None:
        raise UserNotFoundError

    return user


# Function to add a new user to the database
def create_user(session: Session, user: CreateAndUpdateUser) -> User:
    user_details = session.query(User).filter(User.CPF == user.CPF).first()

    if user_details is not None:
        raise UserAlreadyExistError

    new_user = User(**user.dict())
    new_user.hashed_password = hash.bcrypt.hash(new_user.hashed_password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


# Function to update details of the user
def update_user(session: Session, _cpf: str, info_update: CreateAndUpdateUser) -> User:
    user = get_user_by_cpf(session, _cpf)

    if user is None:
        raise UserNotFoundError

    user.name = info_update.name
    user.email = info_update.email
    user.country = info_update.country
    user.state = info_update.state
    user.city = info_update.city
    user.postal_code = info_update.postal_code
    user.street = info_update.street
    user.number = info_update.number
    user.complement = info_update.complement
    user.CPF = info_update.CPF
    user.PIS = info_update.PIS
    user.hashed_password = hash.bcrypt.hash(info_update.hashed_password)

    session.commit()
    session.refresh(user)

    return user


# Function to delete a user from the db
def delete_user(session: Session, _cpf: str):
    user = get_user_by_cpf(session, _cpf)

    if user is None:
        raise UserNotFoundError

    session.delete(user)
    session.commit()

    return

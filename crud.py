from typing import List
from sqlalchemy.orm import Session
from exceptions import UserAlreadyExistError, UserNotFoundError
from models import User
from schemas import CreateAndUpdateUser


# Function to get list of users
def get_all_users(session: Session) -> List[User]:
    return session.query(User).all()


# Function to  get info of a particular user
def get_user_by_id(session: Session, _id: int) -> User:
    user = session.query(User).get(_id)

    if user is None:
        raise UserNotFoundError

    return user


# Function to add a new user to the database
def create_user(session: Session, user: CreateAndUpdateUser) -> User:
    user_details = session.query(User).filter(User.CPF == user.CPF).first()
    if user_details is not None:
        raise UserAlreadyExistError

    new_user = User(**user.dict())
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


# Function to update details of the user
def update_user(session: Session, _id: int, info_update: CreateAndUpdateUser) -> User:
    print("update user, antes")
    user = get_user_by_id(session, _id)
    print("pegou user")

    if user is None:
        raise UserNotFoundError

    user.nome = info_update.nome
    user.email = info_update.email
    user.pais = info_update.pais
    user.estado = info_update.estado
    user.municipio = info_update.municipio
    user.CEP = info_update.CEP
    user.rua = info_update.rua
    user.numero = info_update.numero
    user.complemento = info_update.complemento
    user.CPF = info_update.CPF
    user.PIS = info_update.PIS
    user.senha = info_update.senha

    session.commit()
    session.refresh(user)

    return user


# Function to delete a user from the db
def delete_user(session: Session, _id: int):
    user = get_user_by_id(session, _id)

    if user is None:
        raise UserNotFoundError

    session.delete(user)
    session.commit()

    return

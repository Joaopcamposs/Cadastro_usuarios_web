from typing import List
from sqlalchemy.orm import Session
from backend.app.exceptions import UserAlreadyExistError, UserNotFoundError
from backend.app.models import User
from backend.app.schemas import CreateAndUpdateUser
import passlib.hash as _hash


# Function to get list of users
async def get_all_users(session: Session) -> List[User]:
    return session.query(User).all()


# Function to  get info of a particular user by CPF
async def get_user_by_cpf(session: Session, _cpf: str) -> User:
    user = session.query(User).filter(User.CPF == _cpf).first()

    if user is None:
        raise UserNotFoundError

    return user


# Function to add a new user to the database
async def create_user(session: Session, user: CreateAndUpdateUser) -> User:
    user_details = session.query(User).filter(User.CPF == user.CPF).first()

    if user_details is not None:
        raise UserAlreadyExistError

    new_user = User(**user.dict())
    new_user.hashed_password = _hash.bcrypt.hash(new_user.hashed_password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


# Function to update details of the user
async def update_user(session: Session, _cpf: str, info_update: CreateAndUpdateUser) -> User:
    user = await get_user_by_cpf(session, _cpf)

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
    user.hashed_password = _hash.bcrypt.hash(info_update.hashed_password)

    session.commit()
    session.refresh(user)

    return user


# Function to delete a user from the db
async def delete_user(session: Session, _cpf: str):
    user = await get_user_by_cpf(session, _cpf)

    if user is None:
        raise UserNotFoundError

    session.delete(user)
    session.commit()

    return


def create_db():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+pymysql://root:password@mysql_db/')
    Session = sessionmaker(engine)
    try:
        with Session.begin() as session:
            session.execute('CREATE DATABASE projetoWeb;')
            session.execute('use projetoWeb;')
            session.execute("""create table users (
                        id int AUTO_INCREMENT PRIMARY KEY,
                        name varchar(50) NOT NULL,
                        email varchar(50) NOT NULL,
                        country varchar(50) NOT NULL,
                        state varchar(50) NOT NULL,
                        city varchar(50) NOT NULL,
                        postal_code varchar(8) NOT NULL,
                        street varchar(50) NOT NULL,
                        number varchar(50) NOT NULL,
                        complement varchar(50),
                        CPF varchar(11) NOT NULL,
                        PIS varchar(50),
                        hashed_password varchar(256) NOT NULL
                        );""")
            session.commit()
    except:
        return "Something went wrong"

    return "created database"

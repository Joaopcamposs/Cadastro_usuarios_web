import jwt
import backend.app.models as models
import backend.app.schemas as schemas
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from backend.app.crud import get_user_by_cpf
from backend.app.database import get_db
from backend.app.exceptions import UserNotFoundError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

JWT_SECRET = "myjwtsecret"


async def authenticate_user_cpf(session: Session, _cpf: str, _password: str):
    user = await get_user_by_cpf(session, _cpf)

    if user is None:
        raise UserNotFoundError

    if not user.verify_password(_password):
        return False

    return user


async def create_token(user: models.User):
    user_info = schemas.User.from_orm(user)

    token = jwt.encode(user_info.dict(), JWT_SECRET)

    return dict(access_token=token, token_type="Bearer")


async def get_current_user(session: Session = Depends(get_db),
                           token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = session.query(models.User).get(payload["id"])
    except:
        raise HTTPException(status_code=401, detail="Invalid CPF or Password")

    return user

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database import Base
import passlib.hash as _hash


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    country = Column(String)
    state = Column(String)
    city = Column(String)
    postal_code = Column(String)
    street = Column(String)
    number = Column(String)
    complement = Column(String)
    CPF = Column(String)
    PIS = Column(String)
    hashed_password = Column(String)

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)

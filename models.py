from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database import Base

class users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    pais = Column(String)
    estado = Column(String)
    municipio = Column(String)
    CEP = Column(String)
    rua = Column(String)
    numero = Column(String)
    complemento = Column(String)
    CPF = Column(String)
    PIS = Column(String)
    senha = Column(String)
from pydantic import BaseModel


# To support creation and update APIs
class CreateAndUpdateUser(BaseModel):
    nome: str
    email: str
    pais: str
    estado: str
    municipio: str
    CEP: str
    rua: str
    numero: str
    complemento: str
    CPF: str
    PIS: str
    senha: str


# To support list and get APIs
class User(CreateAndUpdateUser):
    id: int

    class Config:
        orm_mode = True

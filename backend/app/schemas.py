from pydantic import BaseModel


# To support creation and update APIs
class CreateAndUpdateUser(BaseModel):
    name: str
    email: str
    country: str
    state: str
    city: str
    postal_code: str
    street: str
    number: str
    complement: str
    CPF: str
    PIS: str
    hashed_password: str


# To support list and get APIs
class User(CreateAndUpdateUser):
    id: int

    class Config:
        orm_mode = True

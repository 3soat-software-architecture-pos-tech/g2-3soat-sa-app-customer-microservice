from pydantic import BaseModel

class Customer(BaseModel):
    id: str
    cpf: str
    name: str
    email: str
    phone: str
    adress: str
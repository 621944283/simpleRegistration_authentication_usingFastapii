from pydantic import BaseModel
from enum import Enum
class UserType(str, Enum):
    superadmin = "super-admin"
    stuff = "stuff"
    customer = "customer"

class UserCreate(BaseModel):
    username: str
    email: str
    type_user: UserType
    password : str
    confirm_password :str
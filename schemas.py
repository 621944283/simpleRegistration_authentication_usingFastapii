from pydantic import BaseModel
from enum import Enum
class UserType(str, Enum):
    Admin = "Admin"
    SuperAdmin = "Super admin"
    User = "User"

class UserCreate(BaseModel):
    username: str
    email: str
    type_user: UserType
    password : str
    confirm_password :str
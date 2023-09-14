from unicodedata import numeric
from schemas import UserType

from sqlalchemy.dialects.postgresql import NUMERIC
from database import Base
from sqlalchemy import Column, Enum,Float,Integer, Numeric,String,Text,Boolean,DateTime,ForeignKey,Date,FLOAT
from sqlalchemy.orm import relationship
from sqlalchemy import Float
from datetime import datetime
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    email= Column(String,unique = True ,nullable=False,index=True)
    type_user = Column(Enum(UserType), nullable=False)
    password = Column(String,nullable=False)

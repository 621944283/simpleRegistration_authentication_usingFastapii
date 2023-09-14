from fastapi import APIRouter,Depends
from requests import Session
from hashing import Hasher
from models import User
from database import get_db
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
import jwt
from datetime import datetime,timedelta
from config import SECRET_KEY,ALGORITHM
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

@router.post("/token",)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    already_user = db.query(User).filter(User.username==form_data.username).first()

    if already_user:
        password = already_user.password
        print(password)
        if Hasher.verify_password(form_data.password,password) :
           data={"sub":form_data.username,"name":form_data.username,"iat": datetime.utcnow(),"exp": datetime.utcnow() + timedelta(minutes=60)}
           jwt_token = jwt.encode(data,SECRET_KEY, algorithm=ALGORITHM)
           


           return {"access_token": jwt_token, "token_type": "bearer"}
        else :
            return {'error':'password is wrong, Please try again'}
    else :
        return{'error': 'Username does not exist!'}
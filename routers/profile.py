from fastapi import APIRouter,Depends,HTTPException,status
from database import get_db
from models import User
import jwt
from routers.login import oauth2_scheme
from requests import Session
from config import SECRET_KEY,ALGORITHM
router = APIRouter()



@router.get('/profile')
async def profile(db:Session=Depends(get_db),token: str = Depends(oauth2_scheme)):
    print(token)
    try :
        decode_token = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        email = decode_token.get('sub')
        user = db.query(User).filter(User.email==email).first()
        if user :
            return {'username':user.username,'email':user.email,'type_user':user.type_user}
        else :
            raise HTTPException(status_code=401 , detail='Invalid credentials')
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='something wrong , here we should handle errors like jwt expiration ..... but this just simple example , but in real project we should hanle more errors')
from fastapi import APIRouter,Depends
from requests import Session
from models import User
from database import get_db
from hashing import Hasher
from schemas import UserCreate
from routers.login import oauth2_scheme
router = APIRouter()
@router.get('/show_all_user')
async def show_users(db:Session=Depends(get_db),token: str = Depends(oauth2_scheme)):
    number_user = db.query(User).all()
    return number_user



@router.post('/register')
async def POST_register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    existing_username = db.query(User).filter(User.username == user.username).first()
    if existing_user :
        return {'error': f'Email {user.email} already exists'}
    if existing_username :
        return {'error': f'Username {user.username} already exists'}
    if user.password != user.confirm_password :
        return {"Error": "Passwords do not match"}
  
    new_user = User(username=user.username, email=user.email, type_user=user.type_user,password = Hasher.get_hash_password(user.password))

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        print(e)
        return {'error': 'An error occurred while registering the user'}

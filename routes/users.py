import sys
sys.path.append(r'E:\Mine\Courses\FASTAPI\Book Trading')

from fastapi import APIRouter ,Depends , HTTPException , status
from fastapi.security import OAuth2PasswordRequestForm , OAuth2PasswordBearer
import schemas
import  models
from database import get_db
from sqlalchemy.orm import Session
from utils import hash , verify
import oauth2
from datetime import datetime , timedelta

router = APIRouter(prefix='/auth'  ,tags= ["Users"])





@router.post("/signup")
def signup(user : schemas.UserIn , db : Session = Depends(get_db)) :
    user.password = hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user) 
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/signin")
def signin(login : OAuth2PasswordRequestForm = Depends() , db : Session = Depends(get_db)) : 
    user = db.query(models.User).filter(models.User.username ==login.username ).one()
    if user is None : 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    if verify(login.password , user.password) == False : 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    access_token_expires = timedelta(minutes=oauth2.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = oauth2.create_access_token(data= {"user_id" :user.id } , expires_delta= access_token_expires)
    return {"access token" : access_token , "token_type" : "bearer"}







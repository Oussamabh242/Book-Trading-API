import sys
sys.path.append(r'E:\Mine\Courses\FASTAPI\Book Trading')
sys.path.append(r'E:\Mine\Courses\FASTAPI\Book Trading\routes')

from typing import Union
from jose import jwt , JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends , HTTPException , status
from datetime import timedelta , datetime
import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data :dict , expires_delta : Union[timedelta , None])->str : 
    to_encode = data.copy()
    if expires_delta : 
        expire = expires_delta+ datetime.utcnow()
    else : 
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode , key = SECRET_KEY , algorithm = ALGORITHM)
    return encoded_jwt

def get_current_user(token : str = Depends(oauth2_scheme)) :

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try : 
        payload = jwt.decode(token= token , key = SECRET_KEY , algorithms= [ALGORITHM])
        id : str = payload.get("user_id")
        if id is None : 
            raise credentials_exception
        token_data =schemas.TokenData(id = id)
    except JWTError as e : 
        raise credentials_exception
    return token_data



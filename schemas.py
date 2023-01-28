from typing import Optional
from pydantic import BaseModel

class UserIn(BaseModel) : 
    full_name : str
    username : str
    password : str

class Login(BaseModel) : 
    username : str
    password : str

class TokenData(BaseModel) :
    id : Optional[str] = None
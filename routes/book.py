import sys
sys.path.append(r'E:\Mine\Courses\FASTAPI\Book Trading')

from fastapi import APIRouter , Depends ,HTTPException , status
from database import get_db
from oauth2 import get_current_user
from schemas import Book
from sqlalchemy.orm import Session
import models


router = APIRouter(prefix="/book" , tags=["Book"]) 

@router.post("/add")
def add_book(book : Book , user = Depends(get_current_user)  , db : Session = Depends(get_db)) : 
    book = dict(book)
    book["owner_id"] = int(user.id)
    new_book = models.Book(**book)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return(new_book)
import sys
sys.path.append(r'E:\Mine\Courses\FASTAPI\Book Trading')

from fastapi import APIRouter , Depends ,HTTPException , status
from database import get_db
from oauth2 import get_current_user
from schemas import Request , TokenData
from sqlalchemy.orm import Session
import models

router = APIRouter(prefix="/request" , tags=["Requests"])  

@router.post("/send")
def send_request(request : Request , user =  Depends(get_current_user) , db : Session = Depends(get_db)  ) : 
    
    print(user.id)
    sender = db.query(models.User).filter(models.User.id == int(user.id)).one()
    reciver = db.query(models.User).filter(models.User.id == request.reciver).one()
    book = db.query(models.Book).filter(models.Book.id == request.book).one()

    if sender and reciver and book : 
        if book.owner_id == reciver.id : 
            if request.content : 
                req = request.dict()
                req["sender"] = int(user.id)
                new_request = models.Request(**req)
                db.add(new_request) 
                db.commit()
                db.refresh(new_request)
                return new_request
    return HTTPException(status_code= status.HTTP_404_NOT_FOUND)


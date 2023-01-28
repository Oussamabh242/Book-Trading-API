import sys
sys.path.append(r'E:\Mine\Courses\FASTAPI\Book Trading')

from sqlalchemy import Boolean , Integer , Column , String  , ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP 
from database import Base

class User(Base) : 
    __tablename__ = "users"
    id = Column(Integer , primary_key = True ,index = True)
    full_name = Column(String , nullable=False )
    username = Column(String ,nullable = False , unique = True )
    password = Column(String , nullable= False )
    created_at = Column(TIMESTAMP(timezone=True) , nullable = False , server_default = text('now()'))

class Book(Base) : 
    __tablename__ = "books"
    id = Column(Integer , primary_key = True ,index = True)
    name = Column(String  ,nullable= False) 
    author = Column(String , nullable= False)
    added_at = Column(TIMESTAMP(timezone=True) , nullable = False , server_default = text('now()'))
    owner_id = Column(Integer , ForeignKey("users.id",ondelete = "CASCADE") , nullable = False )
    stopped = Column(Boolean , server_default = 'False' , nullable = False )

class Request(Base) : 
    __tablename__ = "requests" 
    id = Column(Integer , primary_key = True ,index = True)
    sender = Column(Integer , ForeignKey("users.id",ondelete = "CASCADE") , nullable = False  )
    reciver = Column(Integer , ForeignKey("users.id",ondelete = "CASCADE") , nullable = False  )
    book = Column(Integer , ForeignKey("books.id",ondelete = "CASCADE") , nullable = False )
    sent_at = Column(TIMESTAMP(timezone=True) , nullable = False , server_default = text('now()'))
    content = Column(String , nullable = False)

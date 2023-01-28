import sys
sys.path.append(r'E:\Mine\Courses\FASTAPI\Book Trading')
sys.path.append(r'E:\Mine\Courses\FASTAPI\Book Trading\routes')


from fastapi import FastAPI 
from database import Base , engine
import models
import routes.users as users

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(users.router)

@app.get("/")
def home() : 
    return {"message" : "hello world"}
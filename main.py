import sys
sys.path.append(r'E:\Mine\Courses\FASTAPI\Book Trading')
sys.path.append(r'E:\Mine\Courses\FASTAPI\Book Trading\routes')


from fastapi import FastAPI 
from database import Base , engine
import models
import routes.users as users
import routes.request as req
import routes.book as bk
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

origins = ["*"]



app = FastAPI()
app.include_router(users.router)
app.include_router(req.router)
app.include_router(bk.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home() : 
    return {"message" : "hello world"}
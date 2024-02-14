from fastapi import FastAPI
from db import session
from models import CEO
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins, 
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def home():
    # this is a controller
    return {"message":"hello world"}


@app.get('/ceos')
def get_ceos():
    ceos = session.query(CEO)
    return ceos.all()
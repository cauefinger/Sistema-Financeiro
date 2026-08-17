from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


DATABASE_URL = "sqlite:///banco.db"

engine = create_engine(DATABASE_URL)

Base = declarative_base() 

'''
uvicorn main:app --reload
http://127.0.0.1:8000

'''
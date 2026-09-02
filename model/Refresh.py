from database import engine, Base
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from datetime import timedelta, timezone, datetime

class Refresh_token(Base):
    __tablename__= "Refresh Tokens"

    id_refresh = Column(Integer, primary_key=True, autoincrement=True)
    sub = Column(String)   
    hash = Column(String)
    date = Column(DateTime,
    default=lambda:
    datetime.utcnow() + timedelta(days=7)
    )
    revogado = Column(Boolean, default=False)
from database import engine, Base
from sqlalchemy import Column, String, Boolean, DateTime
from datetime import timedelta, timezone, datetime
class Refresh_token(Base):
    __tablename__= "Refresh Tokens"

    id_refresh = Column(int, primary_key=True, autoincrement=True)
    sub = Column(String)   
    hash = Column(String)
    date = Column(DateTime)
    revogado = Column(Boolean, default=False)
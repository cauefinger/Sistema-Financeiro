from sqlalchemy import ForeignKey, Column, Integer, Float, String, Boolean
from enum import Enum
from sqlalchemy import Enum as SQLENum, Date
from database import Base
from database import engine


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, default=True)
    admin = Column("admin", Boolean, default=False) 
from sqlalchemy import ForeignKey, Column, Integer, Float, String, Boolean
from enum import Enum
from sqlalchemy import Enum as SQLENum, Date
from database import Base
from database import engine


class Categoria(Base):
    __tablename__ = "categoria"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    nome = Column("nome", String, nullable=False)
    usuario_id = Column("usuario", Integer, ForeignKey("usuarios.id"))

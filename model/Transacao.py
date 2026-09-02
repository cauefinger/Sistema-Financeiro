from sqlalchemy import ForeignKey, Column, Integer, Float, String, Boolean
from enum import Enum
from sqlalchemy import Enum as SQLENum, Date
from database import engine, Base
from enums import TipoTransacao
from controller.auth_router import Usuario

class Transacao(Base):
    __tablename__ = "transacoes"
    descricao = Column("Descricao", String)
    valor = Column("Valor", Float, nullable=False)
    tipo = Column(SQLENum(TipoTransacao), nullable=False)
    data = Column(Date, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

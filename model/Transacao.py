from sqlalchemy import ForeignKey, Column, Integer, Float, String
from sqlalchemy import Enum as SQLENum, Date
from database import Base
from enums import TipoTransacao, Categoria


class Transacao(Base):
    __tablename__ = "transacoes"
    id = Column(Integer, primary_key=True)
    descricao = Column("Descricao", String)
    valor = Column("Valor", Float, nullable=False)
    tipo = Column(SQLENum(TipoTransacao), nullable=False)
    data = Column(Date, nullable=False)
    usuario_id = Column(Integer,ForeignKey("usuarios.id"), nullable=False)
    conta_id = Column(Integer, ForeignKey("conta.id"), nullable=False)
    categoria = Column(SQLENum(Categoria), nullable=False)
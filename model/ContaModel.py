from database import Base
from sqlalchemy import Column, ForeignKey, Integer, Float

class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True, nullable=False)
    saldo = Column(Float, default=0)
    usuario_id = Column(ForeignKey("usuarios.id"), Integer, nullable=False)

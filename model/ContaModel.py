from database import Base
from sqlalchemy import Column, ForeignKey, Integer

class Conta(Base):
    __tablename__ = "Conta"
    id = Column()
    saldo = Column()
usuario_id = Column(ForeignKey("usuarios.id"), Integer, nullable=False)

from sqlalchemy import ForeignKey, Column, Integer, Float, String, Boolean
from enum import Enum
from sqlalchemy import Enum as SQLENum, Date
from database import Base, engine



class TipoTransacao(str, Enum):
    RECEITA = "RECEITA"
    DESPESA = "DESPESA"


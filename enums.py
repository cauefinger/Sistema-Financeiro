from enum import Enum


class StatusTransacao(str, Enum):

    ENTRADA = "entrada"
    SAIDA = "saida"
    TRANSFERENCIA = "transferencia"

class TipoTransacao(str, Enum):
    RECEITA = "RECEITA"
    DESPESA = "DESPESA"
    CANCELADA = "CANCELADA"
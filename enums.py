from enum import Enum


class StatusTransacao(str, Enum):

    ENTRADA = "entrada"
    SAIDA = "saida"
    TRANSFERENCIA = "transferencia"

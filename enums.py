from enum import Enum


class StatusTransacao(str, Enum):

    ENTRADA = "entrada"
    SAIDA = "saida"
    TRANSFERENCIA = "transferencia"

class TipoTransacao(str, Enum):
    RECEITA = "RECEITA"
    DESPESA = "DESPESA"

class Categoria(str, Enum):
    NECESSIDADES = "NECESSIDADES"
    LAZER = "LAZER"
    DIVIDAS = "DIVIDAS"
    INVESTIMENTO = "INVESTIMENTO"
    RENDA_EXTRA = "RENDA_EXTRA"
    TRANSFERENCIA = "TRANSFERANCIA"
    SALARIO = "SALARIO"
    TRANSPORTE = "TRANSPORTE"
    MORADIA = "MORADIA"
    SAUDE = "SAUDE"

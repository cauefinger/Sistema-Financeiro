from schemas import TransacaoSchemas
from fastapi import Depends
from sqlalchemy import Session
from controller.Depends import verificar_token, pegar_sessao
from pydantic import BaseModel
from sqlalchemy.orm import Session
 
def criar_transacao(
transacao: TransacaoSchemas,
sessao: Session = Depends(pegar_sessao),
usuario_atual: dict = Depends(verificar_token)):
    pass
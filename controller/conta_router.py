from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from controller.depends import pegar_sessao, verificar_token
from model.ContaModel import Conta

conta_router = APIRouter(
    prefix="/conta",
    tags="Conta"
    )

#TODO: Não esta aparecendo no docs nem funcionando o endpoint, entender
#TODO: renomear essa funcao para um nome mais descritivo que siga o padrao REST

@conta_router.get("/")
def consultar_saldo(
    sessao: Session = Depends(pegar_sessao),        
    usuario_atual: Session = Depends(verificar_token),
):

    conta = sessao.query(Conta).filter(Conta.usuario_id == usuario_atual.id).first()

    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada.")

    return {
        "saldo": conta.saldo
    }
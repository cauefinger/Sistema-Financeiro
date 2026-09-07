from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from controller.Depends import pegar_sessao, verificar_token
from model.ContaModel import Conta
from model.Usuario import Usuario

conta_router = APIRouter()

@conta_router.get("/conta")
def consultar_saldo(
    sessao: Session = Depends(pegar_sessao),
    usuario_atual: Session = Depends(verificar_token),

):

    conta = sessao.query(Conta).filter(Conta.usuario_id == usuario_atual.id).first()

    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada.")

    return{
        "saldo": conta.saldo
    }
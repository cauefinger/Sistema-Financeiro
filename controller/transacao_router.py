from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from controller.Depends import verificar_token
from sqlalchemy.orm import Session
from controller.Depends import pegar_sessao 
transacao_router = APIRouter (
    prefix= "/transacoes",
    tags=["transacao"]
)

@transacao_router.get("/")
async def listar_transacoes(
    verificacao = Depends(verificar_token),
    sessao: Session = Depends(pegar_sessao)
):
    return {"mensagem": "Rota de transações"}

    
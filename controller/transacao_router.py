from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from controller.Depends import verificar_token
from sqlalchemy.orm import Session
from controller.Depends import pegar_sessao 
from service.Transacao_service import criar_transacao, mostrar_transacao, excluir_transacao
from schemas import TransacaoSchemas

transacao_router = APIRouter (
    prefix= "/transacoes",
    tags=["transacao"]
)

@transacao_router.get("/")
async def transacoes(
    verificacao = Depends(verificar_token),
    sessao: Session = Depends(pegar_sessao)
):
    return mostrar_transacao (
        sessao=sessao,
        usuario_atual=verificacao
    )

@transacao_router.post("/transacoes")
async def criar(
    transacao: TransacaoSchemas,
    sessao: Session = Depends(pegar_sessao),
    usuario_atual: dict = Depends(verificar_token)
):
    return criar_transacao(transacao=transacao, sessao=sessao, usuario_atual=usuario_atual)


@transacao_router.delete("/transacoes_excluir")
async def excluir(
        transacao_id: int,
        sessao: Session = Depends(pegar_sessao),
        usuario_atual: dict = Depends(verificar_token)
):
    return excluir_transacao(
        transacao_id=transacao_id,
        sessao=sessao,
        usuario_atual=usuario_atual
    )
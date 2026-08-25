from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
transacao_router = APIRouter (
    prefix= "/transacoes",
    tags=["trasação"]
)

@transacao_router.get("/")
async def mensagem_rota():
    return {"mensagem":"Você entrou na rota de transações."}   
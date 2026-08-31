from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from controller.Depends import verificar_token
from controller import Depends
transacao_router = APIRouter (
    prefix= "/transacoes",
    tags=["trasação"]
)

@transacao_router.get("/")

async def entrar_rota(
        entrar_rota = Depends(verificar_token)
        ):
        return {"mensagem": "Você está autenticado e entrou na rota de transações."}
    
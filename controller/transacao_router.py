from fastapi import APIRouter

transacao_router = APIRouter (
    prefix= "/transacoes",
    tags=["trasação"]
)

@transacao_router.get("/")
async def mensagem_rota():
    return {"mensagem":"Você entrou na rota de transações."}   
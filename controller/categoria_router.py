from fastapi import APIRouter

categoria_router = APIRouter (
    prefix= "/categorias",
    tags=["categorias"]
)

@categoria_router.get("/")
async def mensagem_rota():
    return {"mensagem":"Você entrou na rota de categoria."}   
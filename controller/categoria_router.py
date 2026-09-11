from fastapi import APIRouter
from service.Categoria_service import buscar_todas_categorias
categoria_router = APIRouter (
    prefix= "/categorias",
    tags=["categorias"]
)

@categoria_router.get("/")
async def mensagem_rota():
    return {"mensagem":"Você entrou na rota de categoria."}   
    return buscar_todas_categorias
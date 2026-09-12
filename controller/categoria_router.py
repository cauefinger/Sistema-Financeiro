from fastapi import APIRouter, Depends
from service.Categoria_service import buscar_todas_categorias
from controller.Depends import pegar_sessao, Session, verificar_token

categoria_router = APIRouter (
    prefix= "/categorias",
    tags=["categorias"]
)

@categoria_router.get("/")
async def mensagem_rota(
    sessao: Session = Depends(pegar_sessao),
    usuario_atual: dict = Depends(verificar_token)
): 
    categrias = buscar_todas_categorias()
    return {"mensagem":"Você entrou na rota de categoria.",
            "categorias": categrias}   
    
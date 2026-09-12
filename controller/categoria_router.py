from fastapi import APIRouter, Depends
from service.Categoria_service import buscar_todas_categorias
from controller.Depends import pegar_sessao, Session, verificar_token
from controller.auth_router import Usuario

categoria_router = APIRouter (
    prefix= "/categorias",
    tags=["categorias"]
)

@categoria_router.get("/")
async def mensagem_rota(
    sessao: Session = Depends(pegar_sessao),
    usuario_atual: Usuario = Depends(verificar_token)
): 
    categrias = buscar_todas_categorias(
        sessao,
        usuario_atual
    )
    return {"mensagem":"Você entrou na rota de categoria.",
            "categorias": categrias}   
    
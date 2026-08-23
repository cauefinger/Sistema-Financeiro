from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Depends import pegar_sessao
from model.Usuario import Usuario
from schemas import VisualizarUsuario


usuario_router = APIRouter (
    prefix= "/usuarios",
    tags=["Usuários"]
)

@usuario_router.get("/", response_model = list[VisualizarUsuario])
async def listar_usuarios(
    sessao: Session = Depends(pegar_sessao)
):
    usuarios = sessao.query(Usuario).all()

    return usuarios

@usuario_router.get("/{id}")
async def listar_usuarios_id(
    id: int,
    sessao: Session = Depends(pegar_sessao)
):
    usuarios_id = sessao.query(Usuario).filter(Usuario.id == id).first()
    return usuarios_id
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controller.Depends import pegar_sessao
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
async def listar_usuario_id(
    id: int,
    sessao: Session = Depends(pegar_sessao)
):
    usuario_id = sessao.query(Usuario).filter(Usuario.id == id).first()
    return usuario_id
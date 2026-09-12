from controller.Depends import pegar_sessao, Session, verificar_token
from fastapi import Depends
from model.Categoria import Categoria
from controller.auth_router import Usuario



def buscar_todas_categorias(
        sessao: Session,
        usuario_atual: Usuario = Depends(verificar_token)
):
        categorias = sessao.query(Categoria).filter(Categoria.usuario_id == usuario_atual.id).all()

        return categorias
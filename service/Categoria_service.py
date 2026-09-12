from controller.Depends import pegar_sessao, verificar_token
from fastapi import Depends
from model import Categoria
from controller.auth_router import Usuario



def buscar_todas_categorias(
        sessao: Session,
        usuario_atual: Usuario = Depends(verificar_token)
):
        categorias = sessao.query(Categoria).filter(Categoria.usuario_id == Usuario.id).all()

        return categorias
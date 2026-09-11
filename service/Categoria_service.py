from controller.Depends import pegar_sessao, Session, verificar_token
from controller import Depends
from model import Categoria
from controller.auth_router import Usuario, Depends


def buscar_todas_categorias(
        sessao: Session = Depends(pegar_sessao),
        usuario_atual: Usuario = Depends(verificar_token)
):
        categorias = sessao.query(Categoria).filter(usuario_atual.id == Usuario.id).all()

        return categorias
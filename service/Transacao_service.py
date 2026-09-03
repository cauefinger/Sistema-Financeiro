from schemas import TransacaoSchemas
from fastapi import Depends
from sqlalchemy.orm import Session
from controller.Depends import verificar_token, pegar_sessao
from pydantic import BaseModel
from model.Transacao import Transacao
from controller.auth_router import Usuario
from model.Categoria import Categoria
from enums import TipoTransacao

def mostrar_transacao(
        sessao: Session = Depends(pegar_sessao),
        usuario_atual: Usuario = Depends(verificar_token)
    ):

        transacoes = sessao.query(Transacao).filter(Transacao.usuario_id == usuario_atual.id).all()
        
        return transacoes
    
    


def criar_transacao(
    transacao: TransacaoSchemas,    
    sessao: Session = Depends(pegar_sessao),
    usuario_atual: Usuario = Depends(verificar_token)):

    nova_transacao = Transacao(
        descricao = transacao.descricao,
        valor = transacao.valor,
        tipo = transacao.tipo,
        data = transacao.data,
        categoria_id = transacao.categoria_id,
        usuario_id = usuario_atual.id
    )

    sessao.add(nova_transacao)
    sessao.commit()
    sessao.refresh(nova_transacao)  

    return nova_transacao


def excluir_transacao(
    transacao: int,
    sessao: Session = Depends(pegar_sessao),
    usuario_atual: Usuario = Depends(verificar_token)
):
        transacao_excluida = sessao.query(Transacao).filter
        (Transacao.id == transacao_id,
        Transacao.usuario_id == usuario_atual.id        
        ).first()


        if transacao_excluida is None:
            return {"mensagem": "Transação excluida com sucesso"}


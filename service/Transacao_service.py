from schemas import TransacaoSchemas
from fastapi import Depends
from sqlalchemy import Session
from controller.Depends import verificar_token, pegar_sessao
from pydantic import BaseModel
from sqlalchemy.orm import Session
from model.Transacao import Transacao

def criar_transacao(
    transacao: TransacaoSchemas,
    sessao: Session = Depends(pegar_sessao),
    usuario_atual: dict = Depends(verificar_token)):

    nova_transacao = Transacao(
        descricao = transacao.descricao,
        valor = transacao.valor,
        tipo = transacao.tipo,
        data = transacao.data,
        categoria_id = transacao.categoria_id,
        usuario_id = usuario_atual["id"]
    )

    sessao.add(nova_transacao)
    sessao.commit()
    sessao.refresh(nova_transacao)  

    return nova_transacao
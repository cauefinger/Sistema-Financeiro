from model.schemas import TransacaoSchemas
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from controller.depends import verificar_token, pegar_sessao
from model.transacao import Transacao
from controller.auth_router import Usuario
from model.conta import Conta
from model.enums import TipoTransacao

def buscar_todas_transacoes(
        sessao: Session,
        usuario_atual: Usuario
    ):

        transacoes = sessao.query(Transacao).filter(Transacao.usuario_id == usuario_atual.id).all()
        
        return transacoes


    
# Criando transação com a operação de adicionar receita ou subtrair despesa integrada

def criar_transacao(
    transacao: TransacaoSchemas,    
    sessao: Session = Depends(pegar_sessao),
    usuario_atual: Usuario = Depends(verificar_token)):

    nova_transacao = Transacao(
        descricao = transacao.descricao,
        valor = transacao.valor,
        tipo = transacao.tipo,
        data = transacao.data,
        usuario_id = usuario_atual.id,
        conta_id = transacao.conta_id,
        categoria = transacao.categoria,

    )
    conta = sessao.query(Conta).filter(Conta.id == transacao.conta_id, Conta.usuario_id == usuario_atual.id).first()

    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada.")

    if transacao.tipo == TipoTransacao.DESPESA:
        conta.saldo -= transacao.valor

    elif transacao.tipo == TipoTransacao.RECEITA:
        conta.saldo += transacao.valor

    sessao.add(nova_transacao)
    sessao.commit()
    sessao.refresh(nova_transacao)  

    return nova_transacao



def excluir_transacao(
    transacao_id: int,
    sessao: Session = Depends(pegar_sessao),
    usuario_atual: Usuario = Depends(verificar_token)
):
    transacao_excluida = sessao.query(Transacao).filter(
        Transacao.id == transacao_id,
        Transacao.usuario_id == usuario_atual.id        
        ).first()


    if transacao_excluida is None:
        raise HTTPException(status_code=404, detail="Transação não encontrada.")

# CONTA

    conta = sessao.query(Conta).filter(Conta.id == transacao_excluida.conta_id,
    Conta.usuario_id == usuario_atual.id
    ).first()


    if conta is None:
        raise HTTPException(status_code=404, detail="Conta da transação não encontrada.")

    if transacao_excluida.tipo == TipoTransacao.DESPESA:
        conta.saldo += transacao_excluida.valor

    elif transacao_excluida.tipo == TipoTransacao.RECEITA:
        conta.saldo -= transacao_excluida.valor 


    sessao.delete(transacao_excluida)
    sessao.commit()

    return {"Mensagem": "Transação excluida com sucesso."}

def buscar_por_id(id: int, sessao: Session = Depends(pegar_sessao)):
    return sessao.query(Transacao).filter(Transacao.id == id).first()

def atualizar_transacao(id: int, transacao_atualizada: TransacaoSchemas, sessao: Session = Depends(pegar_sessao)):
    transacao_existente = buscar_por_id(id, sessao)

    if transacao_existente is None:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    conta = sessao.query(Conta).filter(Conta.id == transacao_existente.conta_id).first()

    if conta is None:
        raise HTTPException(status_code=404, detail="Conta da transação não encontrada.")

    # 1) desfaz o efeito da transação ANTIGA no saldo
    if transacao_existente.tipo == TipoTransacao.DESPESA:
        conta.saldo += transacao_existente.valor
    elif transacao_existente.tipo == TipoTransacao.RECEITA:
        conta.saldo -= transacao_existente.valor

    # 2) atualiza os dados da transação
    transacao_existente.valor = transacao_atualizada.valor
    transacao_existente.data = transacao_atualizada.data
    transacao_existente.descricao = transacao_atualizada.descricao
    transacao_existente.tipo = transacao_atualizada.tipo
    transacao_existente.categoria = transacao_atualizada.categoria

    # 3) aplica o efeito da transação NOVA no saldo
    if transacao_existente.tipo == TipoTransacao.DESPESA:
        conta.saldo -= transacao_existente.valor
    elif transacao_existente.tipo == TipoTransacao.RECEITA:
        conta.saldo += transacao_existente.valor

    sessao.commit()
    sessao.refresh(transacao_existente)

    return transacao_existente
from datetime import timedelta, datetime
from sqlalchemy.orm import Session
from database import engine
from controller.auth_security import gerar_refresh_token, gerar_hash
from model.refresh import Refresh_token

def criar_refresh_token(usuario_id: int, dias_expiracao: int = 7):
    token = gerar_refresh_token() # palavra aleatória
    token_hash = gerar_hash(token) # palavra aleatória codificada
    expiracao = datetime.utcnow() + timedelta(days=7)


    with Session(engine) as session:
        session.add(Refresh_token(
            sub=str(usuario_id),
            hash = token_hash,
            date = expiracao,
            revogado=False
        ))
        session.commit()
    return token


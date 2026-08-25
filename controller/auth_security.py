from jose import jwt
from criptografar import SECRET_KEY
from datetime import timedelta, datetime

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def criar_token(usuario_id):
    expiracao = datetime.utcnow() + timedelta(
        minutes = ACCESS_TOKEN_EXPIRE_MINUTES
    )

    dados = {
        "sub": str(usuario_id),
        "exp": expiracao
    }

    token = jwt.encode(
    dados,
    SECRET_KEY,
    algorithm=ALGORITHM
    )

    return token
from jose import jwt
from criptografar import SECRET_KEY
from datetime import timedelta, datetime
import secrets
import hashlib
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

def gerar_refresh_token() -> str:
    return secrets.token_hex(64) # palavra aleatória

def gerar_hash(token):
    token_bytes = token.encode("utf-8")

    hash_token = hashlib.sha256(token_bytes).hexdigest()

    return hash_token
    
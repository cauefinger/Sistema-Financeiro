from controller.auth_security import gerar_refresh_token, gerar_hash

def criar_refresh_token(usuario_id: int):
    token = gerar_refresh_token() # palavra aleatória
    token_hash = gerar_hash(token) # palavra aleatória codificada
    return token


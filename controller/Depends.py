from database import engine
from sqlalchemy.orm import sessionmaker,session
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from controller.auth_security import SECRET_KEY, ALGORITHM
from model.Usuario import Usuario

from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="autentificacao/login")

def pegar_sessao():

    try:
        Sessao = sessionmaker(bind=engine)
        sessao = Sessao()
        yield sessao

    finally:
        sessao.close()



def verificar_token(token: str = Depends(oauth2_scheme), sessao: session = Depends(pegar_sessao)):

    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_usuario = int(dic_info.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso negado, verifique a validade do token.") 

    usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401,detail="Acesso inválido.")

    return usuario
            
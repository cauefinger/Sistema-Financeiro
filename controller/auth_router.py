from fastapi import APIRouter, Depends, HTTPException
from schemas import UsuarioSchemas, LoginSchemas, SchemaRefresh
from controller.Depends import pegar_sessao
from model.Usuario import Usuario
from criptografar import bcrypt_context, CryptContext
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from controller.auth_security import gerar_hash, gerar_refresh_token, criar_token, oauth2_scheme    
from sqlalchemy import select
from model.Refresh import Refresh_token
from service.token import criar_refresh_token
from datetime import datetime, timedelta, timezone
from database import engine

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

auth_router = APIRouter (
    prefix= "/autentificacao",
    tags=["autentificação"]
)

@auth_router.get("/")
async def mensagem_rota():
    return {"mensagem":"Você entrou na rota de autentificação."}


@auth_router.get("/listar_usuarios")
async def listar_usuarios(sessao = Depends(pegar_sessao)):
    usuarios = sessao.query(Usuario).all()
    return {"A lista de usuários é": usuarios}



@auth_router.post("/")
async def criar_conta(usuario_schema: UsuarioSchemas, sessao = Depends (pegar_sessao)):

    usuario = sessao.query(Usuario).filter(Usuario.email==usuario_schema.email).first()

    if usuario:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")

    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(
            nome = usuario_schema.nome, email = usuario_schema.email, senha = senha_criptografada
            )
        sessao.add(novo_usuario)
        sessao.commit()
        return {"mensagem": f"Usuário cadastrado com sucesso {novo_usuario.email}"} 


def autentificar_usuario(email, senha, sessao):
    usuario = sessao.query(Usuario).filter(Usuario.email == email).first()

    if not usuario or not pwd_context.verify(senha, usuario.senha): 
        raise HTTPException(status_code=401, detail= "Credenciais inválidas.")

    return usuario


@auth_router.post("/login")
async def logar_conta(
        form_data: OAuth2PasswordRequestForm = Depends(),
        sessao: Session = Depends(pegar_sessao)
    ):

    usuario = autentificar_usuario(form_data.username, form_data.password, sessao)

    token = criar_token(usuario.id)
    refresh_token = criar_refresh_token(usuario.id)

    return{
    "refresh_token": refresh_token,
    "access_token": token,
    "token_type": "bearer"
}    


@auth_router.post("/refresh")
def refresh(req: SchemaRefresh):

    with Session(engine) as session:

        token_hash = gerar_hash(req.refresh_token)
        refresh = session.scalar(
            select(Refresh_token).where
            (Refresh_token.hash == token_hash)
        )

        if not refresh:
            raise HTTPException(status_code=401, detail="Refresh token inválido.")

        if refresh.date < datetime.utcnow():
            raise HTTPException(status_code=401, detail="Refresh token expirado.")

        acess = criar_token(refresh.sub)

    return {
        "acess_token": acess,
        "token_tipe": "bearer"
    }


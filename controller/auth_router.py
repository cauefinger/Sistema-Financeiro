from fastapi import APIRouter, Depends, HTTPException
from schemas import UsuarioSchemas, LoginSchemas
from Depends import pegar_sessao
from model.Usuario import Usuario
from criptografar import bcrypt_context, CryptContext
from sqlalchemy.orm import Session
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
    usuario = sessao.query(Usuario).filter(email == Usuario.email).first()

    if not usuario or not pwd_context.verify(senha, usuario.senha_hash): 
        raise HTTPException(status_code=401, detail= "Credenciais inválidas.")

    return usuario

@auth_router.post("/")
async def logar_conta(
    login: LoginSchemas,
    sessao: Session = Depends(pegar_sessao)
    ):

    usuario = autentificar_usuario(login.email,login.senha, sessao)
        
    return{
    
    "mensagem": "Login realizado com sucesso!"
}    
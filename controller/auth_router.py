from fastapi import APIRouter, Depends, HTTPException
from schemas import UsuarioSchemas, LoginSchemas
from Depends import pegar_sessao
from model.Usuario import Usuario
from criptografar import bcrypt_context

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


@auth_router.post("/")
async def logar_conta(
    LoginSchemas,
    Sessao: pegar_sessao
    ):

    Usuario = Sessao.query(Usuario.usuario).filter(Usuario == LoginSchemas.usuario).first()

    if not Usuario:
        raise HTTPException(
            status_code=401,
            detail="Usuário não autorizado ou credenciais inválidas"
        )

    if not bcrypt_context.verify(   # verificação de credenciais
        LoginSchemas.senha,
        Usuario.senha
    ):
        raise HTTPException(
            status_code=401, 
            detail="Usuário não autorizado ou credenciais inválidas"
    )
            

    return{
    
    "mensagem": "Login realizado com sucesso!"
}    
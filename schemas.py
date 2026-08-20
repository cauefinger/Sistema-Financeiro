from pydantic import BaseModel
from typing import Optional
from sqlalchemy import ForeignKey, String, Integer, Boolean, Float, Date
from model.Usuario import Usuario
from enums import StatusTransacao

class UsuarioSchemas(BaseModel):
    nome: String
    email: String
    senha: String
    ativo: Optional[bool]
    admin: Optional[bool]

class VisualizarUsuario(BaseModel):
    nome: String
    email: String
    ativo: Optional[bool]
    admin: Optional[bool]

class VisualizarUsuarioID(BaseModel):
    id: Integer

class LoginSchemas(BaseModel):
    email: String
    senha: String

class TransacaoSchemas(BaseModel):
    id = Integer
    descricao = String
    valor = Float
    tipo = StatusTransacao
    data = Date
    usuario_id = ForeignKey(Usuario.id)

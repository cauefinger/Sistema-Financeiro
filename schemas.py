from pydantic import BaseModel
from typing import Optional
from enums import StatusTransacao
from datetime import date
from sqlalchemy import String
class UsuarioSchemas(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool] = None
    admin: Optional[bool] = None

class VisualizarUsuario(BaseModel):
    nome: str
    email: str
    ativo: Optional[bool] = None
    admin: Optional[bool] = None

class VisualizarUsuarioID(BaseModel):
    id: int

class LoginSchemas(BaseModel):
    email: str
    senha: str

class TransacaoSchemas(BaseModel):
    id: int
    descricao: str
    valor: float
    tipo: str  # Usar str em vez do enum diretamente
    data: date
    usuario_id: int
    categoria_id: int  # Adicionar categoria

class SchemaRefresh(BaseModel):
    Refresh_token: str
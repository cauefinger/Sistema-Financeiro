from pydantic import BaseModel
from typing import Optional
from model.enums import TipoTransacao, Categoria
from datetime import date


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
    descricao: str
    valor: float
    tipo: TipoTransacao  
    data: date
    conta_id: int
    categoria: Categoria

class SchemaRefresh(BaseModel):
    Refresh_token: str

    
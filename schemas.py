from pydantic import BaseModel
from typing import Optional

class UsuarioSchemas(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

class VisualizarUsuario(BaseModel):
    nome: str
    email: str
    ativo: Optional[bool]
    admin: Optional[bool]

class VisualizarUsuarioID(BaseModel):
    id: int

class LoginSchemas(BaseModel):
    email: str
    senha: str

from pydantic import BaseModel
from typing import Optional

class UsuarioSchema(BaseModel):
    foto: str
    nome: str
    email: str
    telefone: str
    cidade: str
    endereco: str
    estado: str
    senha: str
    admin: Optional[bool]
    status: Optional[bool]

    class Config:
        from_attributes = True

class FisioterapeutaSchema(BaseModel):
    nome: str
    email: str
    especialidade: str
    telefone: str
    cidade: str
    endereco: str
    estado: str
    crefito: str
    senha: str
    admin: Optional[bool]
    status: Optional[bool]

    class Config:
        from_attributes = True
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session, joinedload
from dependencies import pegar_sessao
from models import Fisioterapeuta


order_router = APIRouter(prefix="/fisioterapeutas", tags=["fisioterapeutas"])

@order_router.get("/cards")
async def criar_cards():
    """
    Essa é a rota padrão dos fisioterapeutas do nosso sistema.
    """
    return {"mensagem": "Você acessou a rota de fisioterapeutas"}
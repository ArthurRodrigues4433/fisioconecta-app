from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session, joinedload
from dependencies import pegar_sessao
from models import Fisioterapeuta


deashboard_router = APIRouter(prefix="/fisioterapeutas", tags=["fisioterapeutas"])

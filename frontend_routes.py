from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

frontend_router = APIRouter()

# Configura o Jinja2 para buscar templates no diretório 'templates'
templates = Jinja2Templates(directory="templates")

@frontend_router.get("/")
async def read_root(request: Request):
    """
    Renderiza a página inicial.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@frontend_router.get("/criar_fisio")
async def read_rooot(request: Request):
    
    return templates.TemplateResponse("cadastro_fisio.html", {"request": request})
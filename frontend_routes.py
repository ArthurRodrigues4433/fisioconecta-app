from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

router_frontend = APIRouter(prefix="/form", tags=["form"])

templates = Jinja2Templates(directory="templates")

@router_frontend.get("/cadastro_usuario", response_class=HTMLResponse)
def cadastro_usuario(request: Request):
    return templates.TemplateResponse("cadastro_usuario.html", {"request": request})

@router_frontend.get("/cadastro_fisio", response_class=HTMLResponse)
def cadastro_fisio(request: Request):
    return templates.TemplateResponse("cadastro_fisio.html", {"request": request})

@router_frontend.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
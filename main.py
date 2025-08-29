from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

# Carrega automaticamente as variáveis de ambiente do arquivo .env
load_dotenv()

# Recupera a SECRET_KEY do arquivo .env
SECRET_KEY = os.getenv("SECRET_KEY")

# Cria a instância principal da aplicação FastAPI
app = FastAPI()

# Monta o diretório 'static' para servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura o bcrypt para criptografia de senhas
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Importa os roteadores
from auth_routes import auth_router
from order_routes import order_router
from frontend_routes import frontend_router

# Inclui as rotas no app principal
app.include_router(auth_router)
app.include_router(order_router)
app.include_router(frontend_router)

# para rodar o codigo, executar no terminal: uvicorn main:app --reload
#pip install passlib[bcrypt]

# Importa a conexão com o banco de dados (db) criada no models.py
from models import db
from sqlalchemy.orm import sessionmaker

# Função que fornece uma sessão do banco para ser usada nas rotas
def pegar_sessao():
    try:
        # Cria a fábrica de sessões, vinculando ao banco configurado em db
        Session = sessionmaker(bind=db)
        # Cria uma sessão do banco
        session = Session()
        # Entrega (yield) a sessão para quem chamar essa função (injeção de dependência no FastAPI)
        yield session
    finally:
        # Quando terminar o uso da sessão, ela é fechada corretamente
        session.close()  # type: ignore

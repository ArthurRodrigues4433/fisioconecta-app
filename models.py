from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils.types import ChoiceType

# Cria a conexão com o banco SQLite
db = create_engine("sqlite:///banco.db")  
# 'echo=True' mostra no console todas as queries SQL executadas (bom para debug)

# Base do SQLAlchemy para criar as classes/tabelas
Base = declarative_base()


# ==============================
# Usuários (Clientes comuns)
# ==============================
class Usuario(Base):
    __tablename__ = "usuarios"  # Nome da tabela no banco

    # Colunas da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)   # ID único, chave primária
    foto = Column("foto", String(200), nullable=True)                  # Foto de perfil (opcional)
    nome = Column("nome", String(100), nullable=False)                 # Nome do usuário
    email = Column("email", String(100), nullable=False, unique=True)                  # Email único obrigatório
    telefone = Column("telefone", String(20), nullable=True)           # Telefone opcional
    cidade = Column("cidade", String(100), nullable=True)              # Cidade
    endereco = Column("rua", String(100), nullable=True)               # Endereço
    estado = Column("estado", String(50), nullable=True)               # Estado
    senha = Column("senha", String(200), nullable=False)               # Senha (ideal usar hash)
    admin = Column("admin", Boolean, default=False)                    # Se é administrador
    status = Column("status", Boolean)                                 # Status ativo/inativo

    # Construtor para facilitar a criação de novos usuários
    def __init__(self, foto, nome, email, telefone, cidade, endereco, estado, senha, admin=False, status=True):
        self.foto = foto
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cidade = cidade
        self.endereco = endereco
        self.estado = estado
        self.senha = senha
        self.admin = admin
        self.status = status



# ==============================
# Fisioterapeutas (profissionais)
# ==============================
class Fisioterapeuta(Base):
    __tablename__ = "fisioterapeutas"  # Nome da tabela no banco

    # Colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)          # ID único
    nome = Column(String(100), nullable=False)                          # Nome do fisioterapeuta
    crefito = Column(String(20), unique=True, nullable=False)           # Registro profissional (único)
    email = Column(String(100), unique=True, nullable=False)            # Email único obrigatório
    senha = Column(String(200), nullable=False)                         # Senha (ideal usar hash)
    telefone = Column(String(20), nullable=True)                        # Telefone
    especialidade = Column(String(100), nullable=False)                 # Especialidade (ex: pediatria)
    cidade = Column(String(100), nullable=True)                         # Cidade
    endereco = Column(String(100), nullable=True)                       # Endereço
    estado = Column(String(50), nullable=True)                          # Estado
    status = Column(Boolean, default=True)                              # Ativo/inativo
    admin = Column(Boolean, default=False)                              # Se é administrador

    # Relacionamento reverso: um fisioterapeuta pode ter vários cards
    cards = relationship("Card", back_populates="fisioterapeuta")

    # Construtor para facilitar a criação de fisioterapeutas
    def __init__(self, nome, crefito, email, senha, telefone, especialidade, cidade, endereco, estado, status=True, admin=False):
        self.nome = nome
        self.crefito = crefito
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.especialidade = especialidade
        self.cidade = cidade
        self.endereco = endereco
        self.estado = estado
        self.status = status
        self.admin = admin
# Importações necessárias do FastAPI e SQLAlchemy
from fastapi  import APIRouter, Depends, HTTPException
from models import Usuario, Fisioterapeuta
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema, FisioterapeutaSchema
from sqlalchemy.orm import Session

# Cria o roteador de autenticação com prefixo /auth
auth_router = APIRouter(prefix="/auth", tags=["auth"])


# -------------------------
# Rota padrão de autenticação
# -------------------------
@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão do nosso sistema.
    """
    return {"mensagem": "Voce acessou a rota padrão de autenticação", "autenticado": False}


# -------------------------
# Criar conta de USUÁRIO
# -------------------------
@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session = Depends(pegar_sessao)):
    # Verifica se já existe um usuário com esse email
    usuario = session.query(Usuario).filter(Usuario.email ==usuario_schema.email).first()  # type: ignore
    if usuario:
        # Caso exista, lança erro HTTP 400
        raise HTTPException(status_code=400, detail="Email de usuario ja existe!")
    else:
        # Criptografa a senha
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        # Cria novo usuário
        novo_usuario = Usuario(
            foto=usuario_schema.foto,
            nome=usuario_schema.nome,
            email=usuario_schema.email,
            telefone=usuario_schema.telefone,
            cidade=usuario_schema.cidade,
            endereco=usuario_schema.endereco,
            estado=usuario_schema.estado,
            senha=senha_criptografada
        )
        # Salva no banco
        session.add(novo_usuario)
        session.commit()

        return {"mensagem": f"Usuario criado com sucesso! {usuario_schema.email}"}
    

# -------------------------
# Criar conta de FISIOTERAPEUTA
# -------------------------
@auth_router.post("/criar_conta_fisio")
async def criar_conta_fisio(fisioterapeuta_schema: FisioterapeutaSchema,session = Depends(pegar_sessao)  # injeta a sessão do banco automaticamente
):
    # Verifica se já existe fisioterapeuta com esse email
    fisioterapeuta = session.query(Fisioterapeuta).filter(Fisioterapeuta.email == fisioterapeuta_schema.email).first()  # type: ignore
    if fisioterapeuta:
        # Caso exista, lança erro HTTP 400
        raise HTTPException(status_code=400, detail="Email ja existe!")
    else:
        # Criptografa a senha
        senha_criptografada = bcrypt_context.hash(fisioterapeuta_schema.senha)

        # Cria novo fisioterapeuta
        novo_fisioterapeuta = Fisioterapeuta(
            email=fisioterapeuta_schema.email,
            nome=fisioterapeuta_schema.nome,
            especialidade=fisioterapeuta_schema.especialidade,
            telefone=fisioterapeuta_schema.telefone,
            cidade=fisioterapeuta_schema.cidade,
            endereco=fisioterapeuta_schema.endereco,
            estado=fisioterapeuta_schema.estado,
            crefito=fisioterapeuta_schema.crefito,
            senha=senha_criptografada
        )
        # Salva no banco
        session.add(novo_fisioterapeuta)
        session.commit()

        return {"mensagem": f"Fisioterapeuta cadastrado com sucesso {fisioterapeuta_schema.email}!"}
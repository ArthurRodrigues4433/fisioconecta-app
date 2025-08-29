# 🏥 FisioConecta  

> Plataforma web para conectar famílias de crianças que precisam de fisioterapia especializada com profissionais próximos.  

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)  
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)  
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green?logo=fastapi)  
![License](https://img.shields.io/badge/license-MIT-lightgrey)  


## 📖 Sobre o Projeto  

O **FisioConecta** nasceu com o objetivo de facilitar a **busca por fisioterapeutas especializados**, permitindo que famílias encontrem profissionais próximos de sua localização de forma prática e rápida.  

🔹 Visualização em **mapa interativo (Leaflet.js)**  
🔹 **Cards informativos** com nome, especialidade, preço e distância  
🔹 Cadastro e autenticação de usuários e fisioterapeutas  
🔹 Estrutura pronta para **agendamento online** e futuras integrações  


## 🚀 Tecnologias Utilizadas  

| Camada            | Ferramentas / Bibliotecas |
|-------------------|----------------------------|
| **Backend**       | FastAPI, Uvicorn, SQLAlchemy, Pydantic, Jinja2, Aiofiles |
| **Frontend**      | HTML5, CSS3, JavaScript, Leaflet.js, OpenStreetMap |
| **Banco de Dados**| SQLite (protótipo) → PostgreSQL/MySQL (produção) |
| **Segurança**     | Passlib (bcrypt), OAuth2/JWT (planejado) |
| **Outros**        | Git/GitHub, Python 3.11+, Dotenv |


## 📂 Estrutura do Projeto  

fisioconecta-app/
├── static/ # CSS, JS e arquivos estáticos
├── templates/ # Páginas HTML renderizadas via Jinja2
├── main.py # Ponto de entrada da aplicação
├── auth_routes.py # Rotas de autenticação
├── frontend_routes.py # Rotas para o frontend
├── order_routes.py # Rotas de agendamentos
├── dependencies.py # Dependências comuns
├── models.py # Modelos de dados (SQLAlchemy)
├── schemas.py # Schemas (Pydantic)
├── banco.db # Banco SQLite (gerado automaticamente)
├── requirements.txt # Dependências do projeto
└── README.md # Documentação


## ⚡ Como Rodar o Projeto  

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/ArthurRodrigues4433/fisioconecta-app.git
cd fisioconecta-app
2️⃣ Crie e ative o ambiente virtual
bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Instale as dependências
bash
Copy code
pip install -r requirements.txt
4️⃣ Execute a aplicação
bash
Copy code
uvicorn main:app --reload
🌍 Sistema rodando: http://127.0.0.1:8000

📑 Documentação Swagger: http://127.0.0.1:8000/docs

🗺️ Funcionalidades
✅ Cadastro de fisioterapeutas

✅ Listagem em mapa interativo

✅ Cards com informações: nome, especialidade, preço, distância

✅ API REST para cadastro e consulta de fisioterapeutas

Endpoints disponíveis:
POST /fisioterapeutas/ → Cadastrar fisioterapeuta

GET /fisioterapeutas/ → Listar fisioterapeutas

----------------
🧭 Roadmap
----------------
 Backend com FastAPI e SQLAlchemy

 Integração com banco SQLite

 Frontend com mapa interativo (Leaflet.js)

 Filtros por cidade, preço e especialidade

 Login e autenticação JWT

 Agendamento de consultas

 Sistema de avaliações

 Migração para PostgreSQL em produção

 Aplicativo mobile (React Native / Flutter)

📸 Demonstração (em breve)


👨‍💻 Autor
Arthur Manoel de Assis Rodrigues
🔗 GitHub

📜 Licença
Este projeto está sob a licença MIT – sinta-se livre para usar e contribuir.
# 🧑‍⚕️ FisioConecta

O **FisioConecta** é um aplicativo web que conecta famílias de crianças que precisam de fisioterapia especializada com profissionais próximos.  
Ele utiliza **FastAPI** no backend, **SQLAlchemy** para o ORM e **SQLite** como banco de dados inicial.  
Para exibir os fisioterapeutas no mapa, é usado **Leaflet.js** integrado com **OpenStreetMap**.  

---

## 🚀 Tecnologias utilizadas

### **Backend**
- [FastAPI](https://fastapi.tiangolo.com/) → Framework moderno e rápido para APIs Python  
- [Uvicorn](https://www.uvicorn.org/) → Servidor ASGI rápido para rodar o FastAPI  
- [SQLAlchemy](https://www.sqlalchemy.org/) → ORM para banco de dados  
- [Pydantic](https://docs.pydantic.dev/) → Validação de dados  
- [Jinja2](https://jinja.palletsprojects.com/) → Renderização de templates HTML  
- [Aiofiles](https://pypi.org/project/aiofiles/) → Suporte para arquivos estáticos  

### **Frontend**
- HTML + CSS (na pasta `templates/` e `static/`)  
- [Leaflet.js](https://leafletjs.com/) → Biblioteca para mapas interativos  
- [OpenStreetMap](https://www.openstreetmap.org/) → Base do mapa gratuita  

### **Banco de Dados**
- **SQLite** (simples, roda em arquivo `.db`, ideal para prototipagem)  
- Compatível com **PostgreSQL / MySQL** caso queira escalar no futuro  

---

## 📂 Estrutura do Projeto

fisioconecta/
│── app/
│   ├── **init**.py
│   ├── main.py           # Ponto de entrada
│   ├── models.py         # Modelos ORM (SQLAlchemy)
│   ├── database.py       # Conexão com banco
│   ├── routes.py         # Rotas da API e páginas
│   ├── schemas.py        # Pydantic (validação)
│── templates/            # HTML (Jinja2)
│   ├── base.html
│   ├── index.html
│   ├── mapa.html
│── static/               # CSS / JS / imagens
│── requirements.txt      # Dependências
│── README.md             # Documentação

## ⚙️ Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/fisioconecta.git
cd fisioconecta

### 2. Criar ambiente virtual


python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

### 3. Instalar dependências


pip install -r requirements.txt

### 4. Criar banco de dados

O SQLAlchemy já cria automaticamente o banco na primeira execução:


uvicorn app.main:app --reload


### 5. Acessar no navegador

* Página inicial → [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Mapa interativo → [http://127.0.0.1:8000/mapa](http://127.0.0.1:8000/mapa)
* Documentação da API (Swagger) → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📌 Endpoints principais (API)

* `POST /fisioterapeutas/` → Cadastrar fisioterapeuta
* `GET /fisioterapeutas/` → Listar fisioterapeutas

## 🗺️ Exemplo de Mapa (`mapa.html`)

O projeto usa **Leaflet.js** para exibir fisioterapeutas no mapa:

```js
var map = L.map('map').setView([-23.55, -46.63], 12);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

{% for f in fisioterapeutas %}
L.marker([{{ f.latitude }}, {{ f.longitude }}]).addTo(map)
    .bindPopup("<b>{{ f.nome }}</b><br>{{ f.especialidade }}<br>R$ {{ f.preco }}");
{% endfor %}
```

## 📊 Roadmap (MVP → Futuro)

### **MVP**

* [x] Cadastro de fisioterapeutas
* [x] Listagem no mapa com localização
* [x] Frontend simples com HTML + CSS

### **Próximas etapas**

* [ ] Filtro por especialidade
* [ ] Login e autenticação de fisioterapeutas
* [ ] Busca por distância (ex: até 10km)
* [ ] Agendamento de consultas pelo app

---

## 👨‍💻 Autor

Projeto criado por **Arthur Manoel de Assis Rodrigues**.
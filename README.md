# TaskFlow - Sistema de Gestao de Tarefas

Sistema web para gerenciamento de tarefas com autenticacao, CRUD completo e painel de acompanhamento.

## Funcionalidades

- Cadastro e login de usuarios
- Criar, editar e excluir tarefas
- Status: Pendente, Em Andamento, Concluido
- Prioridade: Baixa, Media, Alta
- Dashboard com visualizacao de todas as tarefas

## Stack

- **Backend:** Python (Flask)
- **Banco:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Autenticacao:** Flask-Login

## Instalacao

```bash
# Clonar repositorio
git clone https://github.com/ncnathalia83838gd-coder/taskflow.git
cd taskflow

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Executar aplicacao
python run.py
```

Acesse: http://localhost:5000

## Estrutura

```
taskflow/
├── app/
│   ├── __init__.py      # Configuracao da aplicacao
│   ├── models.py        # Modelos de dados
│   ├── routes.py        # Rotas da aplicacao
│   ├── templates/       # Templates HTML
│   └── static/          # Arquivos estaticos
├── tests/               # Testes
├── requirements.txt     # Dependencias
└── run.py               # Ponto de entrada
```

## Status do Projeto

Em desenvolvimento ativo.

## Equipe

- **Tech Lead / Developer:** IA
- **QA Engineer Junior:** Nana
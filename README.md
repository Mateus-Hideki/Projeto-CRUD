# Projeto CRUD

Sistema de gerenciamento de estoque e cadastro de produtos em Django, com foco no CRUD de peças, modelos e categorias.

## Visão geral

Este projeto permite:
- cadastrar peças de roupa
- cadastrar categorias
- cadastrar modelos
- editar registros existentes
- excluir itens do estoque
- visualizar o painel inicial com resumo do cadastro

A interface foi pensada para uma apresentação de CRUD em estilo premium, com paleta em preto, branco e cinza.

## Requisitos

- Python 3.10+
- SQLite (incluído no projeto)

## Como rodar na sua máquina

### 1) Baixar o projeto

Instale o Git e o Python 3.10 ou superior. Depois, clone o repositório usando a URL do projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>
```

Se o projeto já estiver baixado, abra um terminal na pasta raiz dele. `<PASTA_DO_PROJETO>` representa o nome da pasta criada pelo clone.

### 2) Criar um ambiente virtual próprio

Cada pessoa deve criar seu próprio ambiente virtual. Não copie a pasta `.venv` de outra máquina.

Windows PowerShell:

```powershell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Caso o PowerShell bloqueie a ativação, execute o comando abaixo apenas na sessão atual e tente ativar novamente:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
```

### 3) Instalar as dependências

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4) Entrar na pasta do projeto Django

```bash
cd <PASTA_DO_DJANGO>
```

Neste projeto, `<PASTA_DO_DJANGO>` é a pasta que contém o arquivo `manage.py`.

### 5) Preparar o banco de dados

```bash
python manage.py migrate
```

Esse comando cria ou atualiza o banco SQLite local da pessoa que está executando o projeto. As migrações necessárias já estão incluídas no repositório.

Não execute `makemigrations` apenas para iniciar o projeto. Use esse comando somente depois de alterar os models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6) Iniciar o servidor local

```bash
python manage.py runserver
```

Abra no navegador o endereço exibido pelo Django, normalmente `http://127.0.0.1:8000/`.

## Acesso ao sistema e painel administrativo

O sistema não possui cadastro de usuários. Todas as telas do estoque exigem login e somente o superusuário pode acessar e alterar os dados.

O projeto cria automaticamente um usuário de demonstração ao executar `migrate` pela primeira vez:

- Usuário: `admin`
- Senha: `admin12345`

Depois, acesse a rota `/login/`. Após o login, o sistema abre o controle de estoque. O painel técnico do Django fica na rota `/admin/`.

Esse usuário e essa senha são apenas para demonstração local. Em produção, troque a senha ou crie outro superusuário com:

```bash
python manage.py createsuperuser
```

## Fluxo principal do CRUD

- `/` - painel inicial com resumo do estoque
- `/roupas/` - lista de peças cadastradas
- `/roupas/novo/` - cadastrar nova peça
- `/modelos/` - lista de modelos
- `/categorias/` - lista de categorias

## Observações

- O projeto usa SQLite, então nenhum serviço externo é necessário.
- O ambiente virtual e o banco SQLite devem ser criados localmente por cada pessoa e não devem ser enviados ao repositório.
- A pasta `frontend/` é opcional e não é obrigatória para rodar o CRUD principal.
- O React foi criado como complemento visual, mas a aplicação funcional e principal é a interface do Django.
- Os comandos devem ser executados a partir da pasta que contém o `manage.py`.

## Estrutura principal

- `Projeto_CRUD/core/` - models, views, forms, templates e CRUD
- `Projeto_CRUD/config/` - configuração do Django
- `frontend/` - front-end auxiliar em React, opcional para apresentação visual

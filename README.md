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
- Django 5+
- SQLite (incluído no projeto)

## Como rodar o projeto

### 1) Entrar na pasta do repositório

```powershell
cd "C:\Users\Kaio Damasceno\Documents\GitHub\Projeto-CRUD"
```

### 2) Ativar o ambiente virtual

```powershell
. .\.venv\Scripts\Activate.ps1
```

### 3) Entrar na pasta do projeto Django

```powershell
cd Projeto_CRUD
```

### 4) Aplicar as migrações do banco

```powershell
python manage.py migrate
```

### 5) Iniciar o servidor local

```powershell
python manage.py runserver 0.0.0.0:8000
```

### 6) Acessar a interface do CRUD

```text
http://127.0.0.1:8000/
```

## Fluxo principal do CRUD

- `/` - painel inicial com resumo do estoque
- `/roupas/` - lista de peças cadastradas
- `/roupas/novo/` - cadastrar nova peça
- `/modelos/` - lista de modelos
- `/categorias/` - lista de categorias

## Painel administrativo do Django

O projeto também possui o painel padrão do Django, mas ele fica em uma rota separada:

```text
http://127.0.0.1:8000/admin/
```

Para acessar esse painel, é necessário criar um superusuário:

```powershell
python manage.py createsuperuser
```

Importante: a interface principal do projeto para apresentação e uso do CRUD é a página `/`, e não o painel `/admin/`.

## Observações

- O projeto usa SQLite, então nenhum serviço externo é necessário.
- O ambiente virtual já está configurado na pasta `.venv` do projeto.
- A pasta `frontend/` é opcional e não é obrigatória para rodar o CRUD principal.
- O React foi criado como complemento visual, mas a aplicação funcional e principal é a interface do Django.
- Caso tenha problemas ao rodar, confirme se o terminal está na pasta correta e se o ambiente virtual foi ativado.

## Estrutura principal

- `Projeto_CRUD/core/` - models, views, forms, templates e CRUD
- `Projeto_CRUD/config/` - configuração do Django
- `frontend/` - front-end auxiliar em React, opcional para apresentação visual

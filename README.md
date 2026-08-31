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

1. Abra o terminal na pasta do projeto:

   ```bash
   cd "C:\Users\Kaio Damasceno\Documents\GitHub\Projeto-CRUD"
   ```

2. Ative o ambiente virtual:

   ```powershell
   . .\.venv\Scripts\Activate.ps1
   ```

3. Entre na pasta do projeto Django:

   ```powershell
   cd Projeto_CRUD
   ```

4. Aplique as migrações do banco:

   ```powershell
   python manage.py migrate
   ```

5. Inicie o servidor local:

   ```powershell
   python manage.py runserver 0.0.0.0:8000
   ```

6. Acesse no navegador:

   ```text
   http://127.0.0.1:8000/
   ```

## Fluxo principal do CRUD

- `/` - página inicial com resumo
- `/roupas/` - lista de peças cadastradas
- `/roupas/novo/` - cadastrar nova peça
- `/modelos/` - lista de modelos
- `/categorias/` - lista de categorias

## Observações

- O projeto usa SQLite, então nenhum serviço externo é necessário.
- O ambiente virtual já está configurado na pasta `.venv` do projeto.
- Caso tenha problemas ao rodar, confirme se o terminal está na pasta correta e se o ambiente virtual foi ativado.

## Estrutura principal

- `Projeto_CRUD/core/` - models, views, forms, templates e CRUD
- `Projeto_CRUD/config/` - configuração do Django
- `frontend/` - front-end auxiliar em React, se quiser complementar visualmente a apresentação

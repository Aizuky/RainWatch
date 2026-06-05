#!/bin/bash

# Instala as dependências
pip install -r requirements.txt

# Cria a estrutura de tabelas do Django no banco
python manage.py migrate

# Roda o seu script para colocar os dados iniciais no banco
python popular_banco.py

# Coleta os arquivos estáticos
python manage.py collectstatic --noinput
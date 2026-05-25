#!/bin/bash

# Instala as dependências
pip install -r requirements.txt

# Coleta os arquivos estáticos (obrigatório para o Django não quebrar o layout)
python3.9 manage.py collectstatic --noinput
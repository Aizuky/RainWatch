import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rainwatch.settings")
django.setup()

from sensores.models import Sensor
from abrigos.models import Abrigo

# Limpa os dados antigos

Sensor.objects.all().delete()
Abrigo.objects.all().delete()

# ─── Popula sensores ───
sensores = [
    {"bairro": "Ibura",            "zona": "Zona Sul",   "chuva_mm": 92, "saturacao": 94, "status": "critico", "populacao": "62k"},
    {"bairro": "Mustardinha",      "zona": "Zona Oeste", "chuva_mm": 84, "saturacao": 88, "status": "critico", "populacao": "28k"},
    {"bairro": "Tejipió",          "zona": "Zona Oeste", "chuva_mm": 77, "saturacao": 79, "status": "alerta",  "populacao": "31k"},
    {"bairro": "Jardim São Paulo", "zona": "Zona Oeste", "chuva_mm": 73, "saturacao": 75, "status": "alerta",  "populacao": "24k"},
    {"bairro": "San Martin",       "zona": "Zona Norte", "chuva_mm": 68, "saturacao": 70, "status": "alerta",  "populacao": "17k"},
    {"bairro": "Cordeiro",         "zona": "Zona Norte", "chuva_mm": 66, "saturacao": 69, "status": "alerta",  "populacao": "22k"},
    {"bairro": "Coque",            "zona": "Centro",     "chuva_mm": 61, "saturacao": 65, "status": "alerta",  "populacao": "22k"},
    {"bairro": "Várzea",           "zona": "Zona Oeste", "chuva_mm": 55, "saturacao": 58, "status": "alerta",  "populacao": "29k"},
    {"bairro": "Afogados",         "zona": "Zona Sul",   "chuva_mm": 45, "saturacao": 47, "status": "normal",  "populacao": "38k"},
    {"bairro": "Boa Viagem",       "zona": "Zona Sul",   "chuva_mm": 22, "saturacao": 23, "status": "normal",  "populacao": "110k"},
    {"bairro": "Casa Forte",       "zona": "Zona Norte", "chuva_mm": 18, "saturacao": 20, "status": "normal",  "populacao": "15k"},
    {"bairro": "Torre",            "zona": "Centro",     "chuva_mm": 31, "saturacao": 33, "status": "normal",  "populacao": "43k"},
]

for s in sensores:
    Sensor.objects.create(**s)

print(f"✅ {Sensor.objects.count()} sensores criados")

# Popula abrigos

abrigos = [
    {"nome": "Escola Municipal Aníbal Fernandes",    "endereco": "R. Padre Inglês, 259 — Boa Vista",        "tipo": "Escola",   "bairro": "Boa Vista",     "capacidade": 200},
    {"nome": "Ginásio Geraldão",                     "endereco": "R. da Soledade, s/n — Cordeiro",          "tipo": "Ginásio",  "bairro": "Cordeiro",      "capacidade": 800},
    {"nome": "Igreja Nossa Sra. do Carmo",           "endereco": "Av. Dantas Barreto, 711 — Santo Antônio", "tipo": "Igreja",   "bairro": "Santo Antônio", "capacidade": 150},
    {"nome": "Escola Estadual João Pessoa",          "endereco": "R. João Pessoa, 456 — Afogados",          "tipo": "Escola",   "bairro": "Afogados",      "capacidade": 300},
    {"nome": "Centro Comunitário do Ibura",          "endereco": "R. do Ibura, 123 — Ibura",                "tipo": "Centro",   "bairro": "Ibura",         "capacidade": 120},
    {"nome": "Igreja Evangélica Assembléia de Deus", "endereco": "R. da Mangueira, 78 — Mangueira",         "tipo": "Igreja",   "bairro": "Mangueira",     "capacidade": 180},
    {"nome": "Escola Municipal Poeta Carlos Pena",   "endereco": "R. Tejipió, 340 — Tejipió",               "tipo": "Escola",   "bairro": "Tejipió",       "capacidade": 250},
    {"nome": "Ginásio do Coque",                     "endereco": "R. do Coque, 89 — Coque",                 "tipo": "Ginásio",  "bairro": "Coque",         "capacidade": 400},
    {"nome": "Centro Social Urbano da Várzea",       "endereco": "Av. da Várzea, 567 — Várzea",             "tipo": "Centro",   "bairro": "Várzea",        "capacidade": 160},
    {"nome": "Escola Municipal Amorim Lima",         "endereco": "R. Mustardinha, 234 — Mustardinha",       "tipo": "Escola",   "bairro": "Mustardinha",   "capacidade": 220},
    {"nome": "Igreja Católica São João Batista",     "endereco": "R. do Mandu, 45 — Alto do Mandu",         "tipo": "Igreja",   "bairro": "Alto do Mandu", "capacidade": 130},
    {"nome": "Escola Estadual Governador Arraes",    "endereco": "R. San Martin, 678 — San Martin",         "tipo": "Escola",   "bairro": "San Martin",    "capacidade": 280},
    {"nome": "Centro Comunitário Torre",             "endereco": "R. da Torre, 321 — Torre",                "tipo": "Centro",   "bairro": "Torre",         "capacidade": 100},
    {"nome": "Escola Municipal Bárbara de Alencar",  "endereco": "Av. Boa Viagem, 1200 — Boa Viagem",       "tipo": "Escola",   "bairro": "Boa Viagem",    "capacidade": 350},
    {"nome": "Igreja Nossa Sra. da Conceição",       "endereco": "R. Casa Forte, 89 — Casa Forte",          "tipo": "Igreja",   "bairro": "Casa Forte",    "capacidade": 140},
]

for a in abrigos:
    Abrigo.objects.create(**a)

print(f"✅ {Abrigo.objects.count()} abrigos criados")
print("🎉 Banco populado com sucesso!")
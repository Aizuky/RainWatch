from django.shortcuts import render
from .models import Sensor

def dashboard(request):
    sensores = Sensor.objects.all()

    criticos = sensores.filter(status="critico")
    alertas  = sensores.filter(status="alerta")
    normais  = sensores.filter(status="normal")
    media_chuva = sum(s.chuva_mm for s in sensores) / sensores.count()

    alertas_feed = [
        {"bairro": "Ibura",        "msg": "Solo com 94% de saturação. Risco iminente.",     "nivel": "critico", "hora": "17:42"},
        {"bairro": "Mustardinha",  "msg": "Sensor sem sinal há 12min. Equipe acionada.",     "nivel": "critico", "hora": "17:31"},
        {"bairro": "Tejipió",      "msg": "77mm acumulados. Limiar crítico em 1h.",          "nivel": "alerta",  "hora": "17:18"},
        {"bairro": "Cordeiro",     "msg": "SMS enviado para 14 líderes comunitários.",        "nivel": "alerta",  "hora": "17:05"},
        {"bairro": "San Martin",   "msg": "Chuva moderada prevista nas próximas 3h.",        "nivel": "alerta",  "hora": "16:50"},
    ]

    contexto = {
        "sensores": sensores,
        "total_criticos": criticos.count(),
        "total_alertas": alertas.count(),
        "total_normais": normais.count(),
        "media_chuva": round(media_chuva, 1),
        "alertas_feed": alertas_feed,
    }
    return render(request, "sensores/dashboard.html", contexto)
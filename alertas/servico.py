
"""Lógica de geração e envio de alertas a partir dos dados dos sensores."""

import json
import logging
import urllib.request
from django.utils import timezone
from .models import Alerta, ConfiguracaoAlerta

logger = logging.getLogger(__name__)


def _mensagem(sensor: dict) -> str:
    nivel = sensor["status"].upper()
    return (
        f"⚠️ RAINWATCH — ALERTA {nivel}\n"
        f"Bairro: {sensor['bairro']} ({sensor['zona']})\n"
        f"Chuva acumulada: {sensor['chuva_mm']} mm\n"
        f"Saturação do solo: {sensor['saturacao']}%\n"
        f"Status: {nivel}\n"
        f"Hora: {timezone.now().strftime('%d/%m/%Y %H:%M')}"
    )


def _enviar_email(destinatario: str, mensagem: str, bairro: str) -> tuple[bool, str]:
    """
    Stub de envio de e-mail.
    Em produção: substituir por django.core.mail.send_mail ou similar.
    """
    try:
        logger.info(f"[EMAIL] Para: {destinatario} | Bairro: {bairro}")
        
        return True, ""
    except Exception as e:
        return False, str(e)


def _enviar_sms(destinatario: str, mensagem: str) -> tuple[bool, str]:
    """
    Stub de envio de SMS.
    Em produção: integrar Twilio, Zenvia, etc.
    """
    try:
        logger.info(f"[SMS] Para: {destinatario}")
        return True, ""
    except Exception as e:
        return False, str(e)


def _enviar_webhook(url: str, payload: dict) -> tuple[bool, str]:
    """Envia JSON via POST para a URL configurada."""
    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status < 400:
                return True, ""
            return False, f"HTTP {resp.status}"
    except Exception as e:
        return False, str(e)


def _disparar(alerta: Alerta, sensor: dict) -> None:
    payload = {
        "bairro": sensor["bairro"],
        "zona": sensor["zona"],
        "nivel": sensor["status"],
        "chuva_mm": sensor["chuva_mm"],
        "saturacao": sensor["saturacao"],
        "timestamp": timezone.now().isoformat(),
    }

    if alerta.canal == "email":
        ok, erro = _enviar_email(alerta.destinatario, alerta.mensagem, sensor["bairro"])
    elif alerta.canal == "sms":
        ok, erro = _enviar_sms(alerta.destinatario, alerta.mensagem)
    elif alerta.canal == "webhook":
        ok, erro = _enviar_webhook(alerta.destinatario, payload)
    else:
        ok, erro = False, "Canal desconhecido"

    alerta.status = "enviado" if ok else "falha"
    alerta.enviado_em = timezone.now() if ok else None
    alerta.erro_detalhe = erro
    alerta.save()


def processar_sensores(sensores: list[dict]) -> list[Alerta]:
    
    configs = ConfiguracaoAlerta.objects.filter(ativo=True)
    criados = []

    for sensor in sensores:
        nivel = sensor.get("status", "normal")
        if nivel == "normal":
            continue

        for cfg in configs:
            if nivel == "alerta" and not cfg.notificar_alerta:
                continue
            if nivel == "critico" and not cfg.notificar_critico:
                continue

            alerta = Alerta.objects.create(
                bairro=sensor["bairro"],
                zona=sensor["zona"],
                nivel=nivel,
                chuva_mm=sensor["chuva_mm"],
                saturacao=sensor["saturacao"],
                canal=cfg.canal,
                destinatario=cfg.destinatario,
                mensagem=_mensagem(sensor),
            )
            _disparar(alerta, sensor)
            criados.append(alerta)

    return criados

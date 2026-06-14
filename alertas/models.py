from django.db import models
from django.utils import timezone


class Alerta(models.Model):
    NIVEL_CHOICES = [
        ("normal",  "Normal"),
        ("alerta",  "Alerta"),
        ("critico", "Crítico"),
    ]
    CANAL_CHOICES = [
        ("email",   "E-mail"),
        ("sms",     "SMS"),
        ("webhook", "Webhook"),
    ]
    STATUS_CHOICES = [
        ("pendente",  "Pendente"),
        ("enviado",   "Enviado"),
        ("falha",     "Falha"),
        ("ignorado",  "Ignorado"),
    ]

    bairro       = models.CharField(max_length=100)
    zona         = models.CharField(max_length=50)
    nivel        = models.CharField(max_length=10, choices=NIVEL_CHOICES)
    chuva_mm     = models.FloatField()
    saturacao    = models.FloatField()
    canal        = models.CharField(max_length=10, choices=CANAL_CHOICES)
    destinatario = models.CharField(max_length=200, help_text="E-mail, telefone ou URL do webhook")
    mensagem     = models.TextField()
    status       = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pendente")
    criado_em    = models.DateTimeField(default=timezone.now)
    enviado_em   = models.DateTimeField(null=True, blank=True)
    erro_detalhe = models.TextField(blank=True)

    class Meta:
        ordering = ["-criado_em"]
        verbose_name = "Alerta"
        verbose_name_plural = "Alertas"

    def __str__(self):
        return f"[{self.nivel.upper()}] {self.bairro} — {self.canal} → {self.destinatario}"


class ConfiguracaoAlerta(models.Model):
    CANAL_CHOICES = [
        ("email",   "E-mail"),
        ("sms",     "SMS"),
        ("webhook", "Webhook"),
    ]

    nome             = models.CharField(max_length=100)
    canal            = models.CharField(max_length=10, choices=CANAL_CHOICES)
    destinatario     = models.CharField(max_length=200)
    ativo            = models.BooleanField(default=True)
    notificar_alerta = models.BooleanField(default=True,  verbose_name="Notificar nível Alerta")
    notificar_critico= models.BooleanField(default=True,  verbose_name="Notificar nível Crítico")
    criado_em        = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Configuração de Alerta"
        verbose_name_plural = "Configurações de Alertas"

    def __str__(self):
        return f"{self.nome} ({self.canal})"

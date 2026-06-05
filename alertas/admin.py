from django.contrib import admin
from .models import Alerta, ConfiguracaoAlerta


@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display  = ("bairro", "nivel", "canal", "destinatario", "status", "criado_em")
    list_filter   = ("nivel", "canal", "status")
    search_fields = ("bairro", "destinatario")
    readonly_fields = ("criado_em", "enviado_em", "erro_detalhe")


@admin.register(ConfiguracaoAlerta)
class ConfiguracaoAlertaAdmin(admin.ModelAdmin):
    list_display = ("nome", "canal", "destinatario", "ativo", "notificar_alerta", "notificar_critico")
    list_filter  = ("canal", "ativo")
    
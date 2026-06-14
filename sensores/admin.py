from django.contrib import admin
from .models import Sensor

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display  = ("bairro", "zona", "chuva_mm", "saturacao", "status", "atualizado")
    list_filter   = ("status", "zona")
    search_fields = ("bairro",)
from django.contrib import admin
from .models import Abrigo

@admin.register(Abrigo)
class AbrigoAdmin(admin.ModelAdmin):
    list_display  = ("nome", "tipo", "bairro", "capacidade")
    list_filter   = ("tipo", "bairro")
    search_fields = ("nome", "bairro")
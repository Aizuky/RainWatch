from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: redirect("sensores:dashboard")),  # raiz -> sensores
    path("abrigos/", include("abrigos.urls")),
    path("alertas/", include("alertas.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("sensores/", include("sensores.urls")),
]

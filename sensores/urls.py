from django.urls import path
from . import views

app_name = "sensores"   # registra o namespace

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
]

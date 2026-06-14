from django.urls import path
from . import views

app_name = "sensores"  

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
]

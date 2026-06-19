from django.urls import path
from .views import estado_equipos

urlpatterns = [
    path("", estado_equipos, name="monitor"),
]

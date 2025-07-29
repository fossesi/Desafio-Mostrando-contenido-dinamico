
from django.urls import path
from .views import empleados

urlpatterns = [
    path("", empleados, name="empleados"),
]

from django.contrib import admin
from django.urls import path

from .views import bienvenida, despedida,saludar,saludar_nombre,hello_type


urlpatterns = [
    path("",bienvenida),
    path("despedida/",despedida),
    path("saludo/",saludar),
    path("saludo/<str:nombre>",saludar_nombre),
    path("kodemia/<str:type>",hello_type)
]



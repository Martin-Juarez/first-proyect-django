from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def bienvenida(request):
    return HttpResponse("Bienvenidos")

def despedida(request):
    return HttpResponse("Hasta luego")

def saludar(request):
    return HttpResponse("Saludando a koders")

def saludar_nombre(request, nombre):
    return HttpResponse(f"Hola {nombre}")

def hello_type(request, type):
    if type == "mentor":
        return HttpResponse("Hola Mentor, aqui son tus clases")
    elif type == "koder":
        return HttpResponse("Hola koder, bienvenido a kodemia")
    else:
        return HttpResponse("vete! no eres bievenido aqui")
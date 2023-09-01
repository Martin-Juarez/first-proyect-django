from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
# Create your views here.


def bienvenida(request):
    return HttpResponse("Bienvenidos")

def despedida(request):
    return HttpResponse("Hasta luego")

def saludar(request):
    return HttpResponse("Saludando a koders")

def saludar_nombre(request, nombre):
    context={"name":nombre} #este sirve para meterle info al template
    template = loader.get_template("templates/base.html")
    return HttpResponse(template.render(context,request))

def saludando_a(request, nombre,tipo):
    context={"name":nombre,"type":tipo} #este sirve para meterle info al template
    template = loader.get_template("myapp/templates/practica.html")
    return HttpResponse(template.render(context,request))


def hello_type(request, type):
    if type == "mentor":
        return HttpResponse("Hola Mentor, aqui son tus clases")
    elif type == "koder":
        return HttpResponse("Hola koder, bienvenido a kodemia")
    else:
        return HttpResponse("vete! no eres bievenido aqui")
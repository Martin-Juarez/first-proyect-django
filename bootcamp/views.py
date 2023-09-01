from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.template import loader

def get_koder(request):
    context = {
    "koders": [
        {'name': 'Martin','ID': '1'},
        {'name': 'Miguel','ID': '2'},
        {'name': 'Pedro','ID': '3'},
        {'name': 'Juan','ID': '4'},
        {'name': 'Pepe','ID': '5'},
    ]}
    template = loader.get_template("templates/koders.html")
    
    return HttpResponse(template.render(context,request))

def list_mentors(request):
    context = {
    'mentors': [
            {
                'name': 'Benjamin',
                'last_name': 'Aguilar',
                'is_active': True
            },
            {
                'name': 'Alfredo',
                'last_name': 'Altamirano',
                'is_active': True
            },
            {
                'name': 'Charles',
                'last_name': 'Lopez',
                'is_active': False
            },
        ]}
    template = loader.get_template("templates/list_mentors.html")
    
    return HttpResponse(template.render(context,request))
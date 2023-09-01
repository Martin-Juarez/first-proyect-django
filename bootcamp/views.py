from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.template import loader

def get_koder(request):
    context = {
    "koders": [
        {'name ': 'Martin','ID': '1'},
        {'name ': 'Miguel','ID': '2'},
        {'name ': 'Pedro','ID': '3'},
        {'name ': 'Juan','ID': '4'},
        {'name ': 'Pepe','ID': '5'}
    ]}
    template = loader.get_template("bootcamp/templates/koders.html")
    
    return HttpResponse(template.render(context,request))

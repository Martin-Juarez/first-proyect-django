from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.template import loader

from bootcamp.models import Koder # aqui se importa el modelo Koder o la database


def list_koder(request):
    koders = Koder.objects.all()

    return HttpResponse(koders)

def get_koder(request,idk):
    koder = Koder.objects.filter(pk=idk)
    print(koder)

    return HttpResponse(f"Founder koder ---->{koder}")





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
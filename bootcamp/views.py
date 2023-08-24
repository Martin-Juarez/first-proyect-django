from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_koder(request):
    koders = {
        1: 'Martin',
        2: 'Miguel',
        3: 'Pedro',
        4: 'Juan',
        5: 'Pepe'
    }
    response_content = "La lista de koders es: \n"
    for key, value in koders.items():
        response_content += f"    {key}: '{value}',\n"
    
    return HttpResponse(response_content)



def get_koders(request, key):
    koders = {
        1: 'Martin',
        2: 'Miguel',
        3: 'Pedro',
        4: 'Juan',
        5: 'Pepe'
    }
    
    selected_name = koders.get(int(key))
    if selected_name is not None:
        response_content = f"El nombre del koder con clave {key} es: {selected_name}"
    else:
        response_content = f"No se encontró un koder con la clave {key}"
    
    return HttpResponse(response_content)

from django.contrib import admin
from django.urls import path

from .views import get_koder


urlpatterns = [
    path("koders/",get_koder),
    #path("koder/<int:key>",get_koders),
    
]

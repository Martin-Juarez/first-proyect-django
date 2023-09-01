
from django.contrib import admin
from django.urls import path

from .views import get_koder,list_mentors


urlpatterns = [
    path("koders/",get_koder),
    path("mentors/",list_mentors),
    #path("koder/<int:key>",get_koders),
    
]

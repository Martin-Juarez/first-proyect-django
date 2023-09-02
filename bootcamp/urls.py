
from django.contrib import admin
from django.urls import path

from .views import list_koder,list_mentors,get_koder


urlpatterns = [
    path("koders/",list_koder),
    path("mentors/",list_mentors),
    path("koders/<int:idk>",get_koder),
    
]

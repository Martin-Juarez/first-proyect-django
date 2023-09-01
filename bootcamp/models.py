from django.db import models

# los modelor heredan del modelo predeterminado de django y cada propiedad representa un atributo de la tabla
# Create your models here.
# las bases de dats se crean con clases y siempre van capitalizadas

class Koder(models.Model):
    '''koder model'''
    STATUSES =[                     #Estas duplas nos guardan los choises que van a ser seleccionados en status o size
        ("active","Active"),
        ("inactive","Inactive"),
        ("finished","Finished")
    ]
    SIZES =[
        ("s","Small"),
        ("m","Medium"),
        ("l","Large")
    ]
    first_name = models.CharField(max_length=255) # -> string
    last_name = models.CharField(max_length=255) # -> string
    generation = models.CharField(max_length=20) # -> string
    email = models.EmailField(unique=True)       # -> emailfield check structure
    phone = models.CharField(max_length=25)      # -> string to add +52 etc etc
    status = models.CharField(max_length=8,choices=STATUSES,default="Active")
    size = models.CharField(max_length=1,choices=SIZES,default="s")
    birthdate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True) # en cuanto se crea se agrega la hora automatico
    updated_at = models.DateTimeField(blank=True,null=True) #puede ser null a nivel django

    #Representar como nos regresa al koder
    def __str__(self):
        return f"FisrtName -> {self.first_name},LastName -> {self.last_name}"



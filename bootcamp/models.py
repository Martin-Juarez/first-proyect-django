from django.db import models

# los modelos heredan del modelo predeterminado de django y cada propiedad representa un atributo de la tabla
# Create your models here.
# las bases de dats se crean con clases y siempre van capitalizadas
# LA FK siempre va en la N y cuando es N a N se pone en la mas chica gerarquicamente
# N mentors -N generations
# 1 generacion - N koders
# 1 bootcamp - N generacionesation


    
class Bootcamp(models.Model):
    '''boocamp model'''
    name = models.CharField(max_length=255,unique=True)
    created_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"name {self.name}"


class Generation(models.Model):
# Generaciones pertenecen a un bootcamp -> 1 bootcamp - N generacionesation
    '''geneation model'''
    number = models.IntegerField()
    created_at= models.DateTimeField(auto_now=True)

# FK
    bootcamp = models.ForeignKey(Bootcamp,models.PROTECT,related_name="generations")  # bootcamp va en singular porque 1 bootcamp tiene muchas generaciones
    def __str__(self):
        return f"number {self.number},bootcamp name {self.bootcamp.name}"

class Koder(models.Model):
    '''koder model'''
    # Koder pertenece a 1 generacion -> 1 generacion - N koders
    STATUSES =[                     #Estas duplas nos guardan los choises que van a ser seleccionados en status o size
        ("active","Active"),
        ("inactive","Inactive"),
        ("finished","Finished")
    ]
    first_name = models.CharField(max_length=255) # -> string
    last_name = models.CharField(max_length=255) # -> string
    email = models.EmailField(unique=True)       # -> emailfield check structure
    phone = models.CharField(max_length=25)      # -> string to add +52 etc etc
    status = models.CharField(max_length=8,choices=STATUSES,default="Active")
    created_at= models.DateTimeField(auto_now=True) #puede ser null a nivel django
    #Representar como nos regresa al koder y como se relacionan las tablas

    generation = models.ForeignKey(Generation,models.PROTECT,related_name="koders") # related_name siempre se llama el nombre de la tabla en plural y con minusculas, siempre se usa PROTECT

    def __str__(self):
        return f"FisrtName -> {self.first_name},LastName -> {self.last_name}"



class Mentor(models.Model):
    '''mentor model'''
    # Mentores pertenece a N generaciones -> N mentors -N generations
    first_name = models.CharField(max_length=255,) # -> string
    last_name = models.CharField(max_length=255) # -> string
    email = models.EmailField(unique=True)       # -> emailfield check structure
    phone = models.CharField(max_length=25)      # -> string to add +52 etc etc
    created_at= models.DateTimeField(auto_now=True) #puede ser null a nivel django
    #Representar como nos regresa al koder

    generations =models.ManyToManyField(Generation,related_name="mentors") # se pone generatios a la variable porque un mentor puede tener muchas generaciones

    def __str__(self):
        return f"id: {self.pk}, {self.first_name},{self.last_name}"
    





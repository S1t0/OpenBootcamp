from this import d
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
# Create your models here.

class Genero(models.Model):#este seria el modelo
    nombre=models.CharField(max_length=64, help_text="Pon el nombre del genero")


    def __str__(self):
        return self.nombre
        #esta funcion nos devuelve nombre en string


class Libro(models.Model):
    titulo=models.CharField(max_length=32)
    autor=models.ForeignKey("Autor", on_delete=models.SET_NULL, null=True)#esto lo que hace es que el autor va a tener un numero, y estar relacionado con otra tabla, sacando los datos de esa otra tabla
    sumario=models.TextField(max_length=100,help_text="Pon aqui de que va el libro")
    isbn=models.CharField("ISBN", max_length=13, help_text="Isbn maximo de 13 caracteres")
    genero=models.ManyToManyField(Genero)#este nos permite que el libro tenga varios generos, aqui le ponemos el genero creado arriba

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("book-detail",args={str(self.id)})



class Autor(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    fecha_de_nacimiento=models.DateField(null=True, blank=True)
    fecha_de_muerte=models.DateField("Died",null=True, blank=True)

    def get_absolute_url(self):
        return reverse("detalle-autor",args=[str(serlf.id)])

    def __str__(self):
        return "%s,%s"%(self.apellido, self.nombre)
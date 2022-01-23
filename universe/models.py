from django.db import models
from django.forms import CharField, EmailField, ImageField, IntegerField

# Create your models here.

class Persona(models.Model):
    id_user=models.CharField(max_length=50)
    name=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(null=True,blank=True)
    photo=models.ImageField(null=True,blank=True)

    class Meta:
        verbose_name="persona"
        verbose_name_plural="Personas"
    
    def __str__(self):
        return (f"{self.id_user}-{self.name} {self.lastname}")
    

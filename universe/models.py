from django.db import models
from django.forms import CharField, EmailField, IntegerField

# Create your models here.

class user(models.Model):
    id=IntegerField()
    name=CharField(max_length=20)
    lastname=CharField(max_length=20)
    email=EmailField()

    

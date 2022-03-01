from django.db import models

# Create your models here.

class Auditor(models.Model):
    id_auditor=models.CharField(max_length=20,primary_key=True)
    name_auditor=models.CharField(max_length=100)
    photo_auditor=models.ImageField()
    operation_center=models.CharField(max_length=50)
    name_zone=models.CharField(max_length=50)


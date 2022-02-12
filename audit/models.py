from datetime import date
from django.db import models
from django.forms import CharField, EmailField, ImageField, IntegerField

# Create your models here.

class Audit(models.Model):
    idAudit=models.CharField(max_length=50,primary_key=True)
    typeAudit=models.CharField(max_length=25)
    auditor=models.CharField(max_length=25)
    zone=models.CharField(max_length=25)
    state=models.CharField(max_length=25)
    city=models.CharField(max_length=25)
    codeAudit=models.CharField(max_length=25)
    ambient=models.CharField(max_length=25)
    ambientDetail=models.CharField(max_length=50)
    datePlan=models.DateField()
    dateExect=models.DateField(blank=True, default=date(1111, 11, 11))
    actDetail=models.CharField(max_length=500)
    status=models.CharField(max_length=25, default="pendiente")


class findings(models.Model):
    idFinding=models.CharField(max_length=50,primary_key=True)
    idAudit=models.CharField(max_length=50)
    alias=models.CharField(max_length=100)
    detailFinding=models.CharField(max_length=500)
    photoEvidence=models.ImageField()
    docEvidence=models.BinaryField()
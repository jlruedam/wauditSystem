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
    dateEject=models.DateField()
    actDetail=models.CharField(max_length=500)
    status=models.CharField(max_length=25, default="pendiente")


# class Auditor(models.Model):
#     documentID=models.CharField(max_length=25)
#     nameAuditor=models.CharField(max_length=50)
    
    
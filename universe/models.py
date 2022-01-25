from django.db import models
from django.forms import CharField, EmailField, ImageField, IntegerField



class UniverseManageResponsable(models.Model):
    codeManage=models.CharField(max_length=5,unique=True)
    responsable=models.CharField(max_length=100)

    def __str__(self):
        return (f"{self.codeManage}-{self.responsable}")
    
class UniverseMacroproces(models.Model):
    numMacro=models.CharField(max_length=5,unique=True)
    macroprocess=models.CharField(max_length=100)
    responsable=models.CharField(max_length=100)
    def __str__(self):
        return (f"{self.numMacro}-{self.macroprocess}-{self.responsable}")
     
    
class UniverseProces(models.Model): 
    process=models.CharField(max_length=100)
    responsable=models.CharField(max_length=100)
    macroprocess=models.CharField(max_length=100)
    def __str__(self):
        return (f"{self.process}-{self.responsable}-{self.macroprocess}")

    

# class AuditUniverse(models.Model):
#     code=models.CharField(max_length=10)
#     generalAudit=models.CharField(max_length=25)
#     audit=models.CharField(max_length=100)
#     activities=models.CharField(max_length=100)
#     risk=models.CharField(max_length=100)
#     priority=models.CharField(max_length=100)
#     macroProcessResponsable=models.CharField(max_length=100)
#     macroProcess=models.CharField(max_length=100)
#     process=models.CharField(max_length=100)
#     place=models.CharField(max_length=100)
#     type=models.CharField(max_length=100)


# class AuditAliasCause(models.Model):
#     code=models.CharField(max_length=10)
#     alias=models.CharField(max_length=200)
#     cause=models.CharField(max_length=200)



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
    

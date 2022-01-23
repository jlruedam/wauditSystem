import email
from django.shortcuts import render
from universe.models import Persona

# Create your views here.

def prueba(request):
    dataPersonas=Persona.objects.all()
    context={
        "dataPersonas":dataPersonas
    }
    return render(request, "./universe/prueba.html",context)

def cargarPersona(request):
   
    nuevaPersona=Persona(
        id_user=request.GET['id_user'],
        name=request.GET['name'],
        lastname=request.GET['lastname'],
        email=request.GET['email'],
    )
    nuevaPersona.save()

    dataPersonas=Persona.objects.all()
    context={
        "dataPersonas":dataPersonas
    }
    return render(request, "./universe/prueba.html",context)

def universeAudit(request):
    return render(request, "./universe/universeAudit.html")



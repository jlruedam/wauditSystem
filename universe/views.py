import email
from django.shortcuts import render
from universe.models import *

# Create your views here.
def processUniverse(request):
    try:
        action=request.POST['action']
        responsable=request.POST['manageResponsableMacro'] 
        cod=request.POST['codeManage'] 
        print("el valor de action es:"+ action)
        context={"responsable":responsable,"action": action, "code":cod}

        if action=="guardar":
            newProcess=UniverseManageResponsable(codeManage=cod,responsable=responsable)
            newProcess.save()
            return render(request, "./universe/processUniverse.html",context )
        else:
            return render(request, "./universe/processUniverse.html", context)
    except Exception as e:
        print("WATAGATAPITUSBERRY!")
        return render(request, "./universe/processUniverse.html")






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




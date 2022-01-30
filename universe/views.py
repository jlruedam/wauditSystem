from dataclasses import dataclass
import email
import http
from multiprocessing.dummy import Process
from django.shortcuts import render
from universe.models import *
from django.http import HttpResponse, JsonResponse


# Create your views here.
def listProcessUniverse(request):

    # Se utiliza esta vista para los queries realizados de forma asíncrona para renderizar listas deplegables dependientes
    # Se utiliza esta misma vista para solicitar diferentes vistas y se utiliza la petición GET para obtener los parametros de busquedas a través de la URL.
    # Los parámetros recibidos son type indica que data voy a filtrar (responsable, proceso, macroproceso) 
    # res-responsable a buscar, 

    search=request.GET['buscar']
    type_data=request.GET['type']
    print("Buscar:" + search)
    print("Tipo: "+type_data)

    if type_data=='responsable':

        macro=[]
        dataMacroProcess=list(UniverseMacroproces.objects.all().filter(responsable=search).values())
        
        for data in dataMacroProcess:
            macro.append(data['macroprocess'])
            
        print(macro)
        return JsonResponse({"dataMacroProcess":macro})
    
    if type_data=='macroprocess':
        process=[]
        dataProcess=list(UniverseProces.objects.all().filter(macroprocess=search).values())
    
        for data in dataProcess:
            print(data)
            process.append(data['numProcess']+"/"+data['process'])
            

        print(process)
        return JsonResponse({"dataProcess":process}) 

    
    # return render(request, "./universe/auditUniverse.html",context) 


def moduleAuditUniverse(request):
    dataManageResponsable=UniverseManageResponsable.objects.all()
    dataMacroProcess=UniverseMacroproces.objects.all()
    dataProcess=UniverseProces.objects.all()
    context={
        "dataManageResponsable":dataManageResponsable,
        # "dataMacroProcess":dataMacroProcess,
        # "dataProcess":dataProcess
    }
    return render(request, "./universe/auditUniverse.html",context)


def moduleProcessUniverse(request):
    dataManageResponsable=UniverseManageResponsable.objects.all()
    dataMacroProcess=UniverseMacroproces.objects.all()
    context={
        "dataManageResponsable":dataManageResponsable,
        "dataMacroProcess":dataMacroProcess,
    }
    return render(request, "./universe/processUniverse.html", context)

def manageResponsableUniverse(request):
    dataManageResponsable=UniverseManageResponsable.objects.all()
    dataMacroProcess=UniverseMacroproces.objects.all()
    # Llamar data de la gestión responsable para actualizar listado en l formulario de macroproceso
    # Por esta misma razón se de dentro del contexto de esta vista

    # Se captura excepción para utilizar el caso inicial cuando la vista se llama desde el botón sin enviar parámetros 
    # a través del POST; es cuando action y manageResponsable no se envian a través del POST.
    try:
    
        action=request.POST['action']
        responsable=request.POST['manageResponsable'] 
        cod=request.POST['codeManage'] 
        responsable=responsable.replace(" ","_")

        context={
            "responsable":responsable,
            "action": action, 
            "code":cod,
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
        }
        # Desde el formulario se envía el parámetro action a través de una etiqueta input no visible, esto
        # permitirá usar una misma vista para varias acciones y se evitan crear tantas URL´s
        if action=="guardar":

            newProcess=UniverseManageResponsable(codeManage=cod,responsable=responsable)
            newProcess.save()
            return render(request, "./universe/processUniverse.html",context )

        else:
            return render(request, "./universe/processUniverse.html", context)

    except Exception as e:

        context={
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
        }
        return render(request, "./universe/processUniverse.html",context)

def macroProcessUniverse(request):
    dataManageResponsable=UniverseManageResponsable.objects.all()
    dataMacroProcess=UniverseMacroproces.objects.all()

    try:
        action=request.POST['action']
        responsable=request.POST['manageResponsableMacro'] 
        macroProcess=request.POST['macroprocessUniverse']
        macroProcess=macroProcess.replace(" ","_")

        context={
            "action": action, 
            "responsable":responsable,
            "macroProcess":macroProcess,
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
            
        }
        # Desde el formulario se envía el parámetro action a través de una etiqueta input no visible, esto
        # permitirá usar una misma vista para varias acciones y se evitan crear tantas URL´s
        if action=="guardar":

            newMacroProcess=UniverseMacroproces(macroprocess=macroProcess,responsable=responsable)
            newMacroProcess.save()
            return render(request, "./universe/processUniverse.html",context )

        else:
            context={
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
            }
            return render(request, "./universe/processUniverse.html", context)

    except:
        
        context={
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
        }
        return render(request, "./universe/processUniverse.html",context)

def processUniverse(request):
    dataManageResponsable=UniverseManageResponsable.objects.all()
    dataMacroProcess=UniverseMacroproces.objects.all()

    try:
        action=request.POST['action']
        responsable=request.POST['manageResponsableProcess'] 
        macroProcess=request.POST['macroprocessUniverse']
        numProcess=request.POST['numberProcessUniverse']
        process=request.POST['processUniverse']
        process=process.replace(" ","_")

        context={
            "action": action, 
            "responsable":responsable,
            "macroProcess":macroProcess,
            "numProcess":numProcess,
            "process":process,
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
        }
        # Desde el formulario se envía el parámetro action a través de una etiqueta input no visible, esto
        # permitirá usar una misma vista para varias acciones y se evitan crear tantas URL´s
        if action=="guardar":

            newProcess=UniverseProces(process=process, numProcess=numProcess, macroprocess=macroProcess, responsable=responsable)
            newProcess.save()
            return render(request, "./universe/processUniverse.html",context )

        else:
            context={
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
            }
            return render(request, "./universe/processUniverse.html", context)

    except:
        print("WATAGAPITUSBERRY")
        context={
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
        }
        return render(request, "./universe/processUniverse.html",context)
    


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




from dataclasses import dataclass
import email
import http
from multiprocessing.dummy import Process
from unicodedata import name
from django.shortcuts import render
from universe.models import *
from django.http import HttpResponse, JsonResponse



#*********Queries
def listProcessUniverse(request):

    

    # Se utiliza esta vista para los queries realizados de forma asíncrona para renderizar listas deplegables dependientes
    # Se utiliza esta misma vista para solicitar diferentes vistas y se utiliza la petición GET para obtener los parametros de busquedas a través de la URL.
    # Los parámetros recibidos son type indica que data voy a filtrar (responsable, proceso, macroproceso) 
    

    search=request.GET['buscar']
    type_data=request.GET['type']
    # print("Buscar:" + search)
    # print("Tipo: "+type_data)

    if type_data=='responsable':

        macro=[]
        dataMacroProcess=list(UniverseMacroproces.objects.all().filter(responsable=search).values())
        
        for data in dataMacroProcess:
            macro.append(data['macroprocess'])
            
        # print(macro)
        return JsonResponse({"dataMacroProcess":macro})
    
    if type_data=='macroprocess':
        process=[]
        dataProcess=list(UniverseProces.objects.all().filter(macroprocess=search).values())
    
        for data in dataProcess:
            # print(data)
            process.append(data['numProcess']+"/"+data['process'])
            

        # print(process)
        return JsonResponse({"dataProcess":process}) 
#*********Modules
def moduleUniverseAudit(request):
    # Muestra el renderizado inicial del módulo Universo Auditable
    dataAuditUniverse=UniverseAudit.objects.all()
    
    context={
        "dataAuditUniverse":dataAuditUniverse,
        
    }

    return render(request, "./universe/moduleUniverseAudit.html",context)
#*********Submodules
def subModuleAuditUniverse(request): 
    # Esta vista muestra el pantallazo inicial del sudmódulo la creación de la auditoría en el universo

    dataManageResponsable=UniverseManageResponsable.objects.all()
    dataMacroProcess=UniverseMacroproces.objects.all()
    dataProcess=UniverseProces.objects.all()
    context={
        "dataManageResponsable":dataManageResponsable,
        # "dataMacroProcess":dataMacroProcess,
        # "dataProcess":dataProcess
    }
    return render(request, "./universe/subModuleAuditUniverse.html",context)

def subModuleProcessUniverse(request):
    # Esta vista muestra el renderizado inicial del submódulo "Proceso Universo"

    dataManageResponsable=UniverseManageResponsable.objects.all()
    dataMacroProcess=UniverseMacroproces.objects.all()
    context={
        "dataManageResponsable":dataManageResponsable,
        "dataMacroProcess":dataMacroProcess,
    }
    return render(request, "./universe/subModuleProcessUniverse.html", context)
    
def subModuleAliasUniverse(request):
    # Esta vista muestra el renderizado inicial del submódulo "Proceso Universo"

    dataAuditUniverse=UniverseAudit.objects.all()
    
    context={
        "dataAuditUniverse":dataAuditUniverse,
        
    }
    return render(request, "./universe/subModuleAliasUniverse.html", context)

#*********load to DataBase
def aliasUniverse(request):

    # Esta vista permite interactuar con el submódulo "Alias Universo", para guardar alias
    # en la base de datos, capturando los datos obtenidos desde el formulario.
    dataAuditUniverse=UniverseAudit.objects.all()
    
    # Se captura excepción para utilizar el caso inicial cuando la vista se llama desde el botón sin enviar parámetros 
    # a través del POST; es cuando action y manageResponsable no se envian a través del POST.
    try:
    
        action=request.POST['action']
        codeAudit=request.POST['selectCodeAudit']
        alias=request.POST['aliasFinding']
        description=request.POST['aliasDescription']

        print("Los datos enviados son:",action, codeAudit,alias,description)

        context={
            
            "dataAuditUniverse":dataAuditUniverse,
            "aliasCreated":alias
        }
        # Desde el formulario se envía el parámetro action a través de una etiqueta input no visible, esto
        # permitirá usar una misma vista para varias acciones y se evitan crear tantas URL´s
        if action=="guardar":

            newAliasUniverse=UniverseAlias(
                codeAudit=codeAudit,
                alias=alias,
                description=description
            )

            newAliasUniverse.save()
            return render(request, "./universe/subModuleAliasUniverse.html",context )

        else:
            return render(request, "./universe/subModuleAaliasUniverse.html", context)

    except Exception as error:
        print("El error es:", error)
        context={
            "dataAuditUniverse":dataAuditUniverse,
            
        }
        return render(request, "./universe/subModuleAliasUniverse.html",context)

def auditUniverse(request):
    # Esta vista permite interactuar con el submódulo "Auditorías Universo", para guardar una auditoria
    # en la base de datos, capturando los datos obtenidos desde el formulario.
    dataManageResponsable=UniverseManageResponsable.objects.all()
    
    # Se captura excepción para utilizar el caso inicial cuando la vista se llama desde el botón sin enviar parámetros 
    # a través del POST; es cuando action y manageResponsable no se envian a través del POST.
    try:
    
        action=request.POST['action']
        responsable=request.POST['selectResponsable'] 
        macroProcess=request.POST['selectMacroprocess']
        process=request.POST['selectProcess']
        numAudit=request.POST['numAuditUniverse']
        code=request.POST['codeAuditUniverse'] 
        generalAudit=request.POST['generalAuditUniverse'] 
        nameAudit=request.POST['nameAuditUniverse']
        activity=request.POST['activityAuditUniverse']
        risk=request.POST['riskAuditUniverse']


        dataProcess=list(UniverseProces.objects.all().filter(numProcess=process).values())

        
    
        context={
            
            "dataManageResponsable":dataManageResponsable,
            "auditCreated":code+"-"+nameAudit
        }
        # Desde el formulario se envía el parámetro action a través de una etiqueta input no visible, esto
        # permitirá usar una misma vista para varias acciones y se evitan crear tantas URL´s
        if action=="guardar":

            newAuditUniverse=UniverseAudit(
                code=code,
                numAudit=numAudit,
                generalAudit=generalAudit,
                audit=nameAudit,
                activities=activity,
                risk=risk,
                responsable=responsable,
                macroProcess=macroProcess,
                process=dataProcess[0]['process']
            )

            newAuditUniverse.save()
            return render(request, "./universe/subModuleAuditUniverse.html",context )

        else:
            return render(request, "./universe/subModuleAuditUniverse.html", context)

    except Exception as e:
        print(e)
        context={
            "dataManageResponsable":dataManageResponsable,
            
        }
        return render(request, "./universe/subModuleAuditUniverse.html",context)

def manageResponsableUniverse(request):
    # Esta vista permite interactuar con el submódulo "Proceso Universo", para guardar una Gestioón responsable
    # en la base de datos, capturando los datos obtenidos desde el formulario.

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
            return render(request, "./universe/subModuleprocessUniverse.html",context )

        else:
            return render(request, "./universe/subModuleprocessUniverse.html", context)

    except Exception as e:
        print(e)
        context={
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
        }
        return render(request, "./universe/subModuleprocessUniverse.html",context)

def macroProcessUniverse(request):
    # Esta vista permite interactuar con el submódulo "Proceso Universo", para guardar un Macproceso
    # en la base de datos, capturando los datos obtenidos desde el formulario.
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
            return render(request, "./universe/subModuleprocessUniverse.html",context )

        else:
            context={
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
            }
            return render(request, "./universe/subModuleprocessUniversee.html", context)

    except:
        
        context={
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
        }
        return render(request, "./universe/subModuleprocessUniverse.html",context)

def processUniverse(request):
    # Esta vista permite interactuar con el submódulo "Proceso Universo", para guardar un Proceso
    # en la base de datos, capturando los datos obtenidos desde el formulario.

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
            return render(request, "./universe/subModuleprocessUniverse.html",context )

        else:
            context={
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
            }
            return render(request, "./universe/subModuleprocessUniverse.html", context)

    except:
        print("WATAGAPITUSBERRY")
        context={
            "dataManageResponsable":dataManageResponsable,
            "dataMacroProcess":dataMacroProcess
        }
        return render(request, "./universe/subModuleprocessUniverse.html",context)
    

# Vistas de Prueba

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






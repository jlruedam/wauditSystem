from multiprocessing import context
from django.shortcuts import render
from universe.models import *
from audit.models import *
from django.http import HttpResponse, JsonResponse

# Create your views here.

#*********Queries
def listUniverse(request):
     # Se utiliza esta vista para los queries realizados de forma asíncrona para renderizar listas deplegables dependientes
    # Se utiliza esta misma vista para solicitar diferentes vistas y se utiliza la petición GET para obtener los parametros de busquedas a través de la URL.
    # Los parámetros recibidos son type indica que data voy a filtrar (codeAudit) 

    search=request.GET['buscar']
    type_data=request.GET['type']
    print("Buscar:" + search)
    print("Tipo: "+type_data)

    if type_data=='code':

        nameAudit=list(UniverseAudit.objects.filter(code=search).values())

        activities=nameAudit[0]['activities']
        audit=nameAudit[0]['audit']
        print(activities)
        print(audit)

        context={
            'audit':audit,
            'activities':activities
        }


        return JsonResponse(context)
    
    return JsonResponse({"dataMacroProcess":"Washinango"})

def listAudit(request):

    search=request.GET['buscar']
    type_data=request.GET['type']
    print("Buscar:" + search)
    print("Tipo: "+type_data)

    if type_data=='idAudit':

        selectedAudit=list(Audit.objects.filter(idAudit=search).values())[0]
        print(selectedAudit)
        return JsonResponse(selectedAudit)
    
    return JsonResponse({"dataMacroProcess":"Washinango"})
     
#*********Modules
def index(request):
    dataAudit=Audit.objects.all()
    context={
        "dataAudit":dataAudit,
    }

    return render(request, "./audit/index.html",context)

#*********Submodules
def subModuleCreateAudit(request):

    dataAuditUniverse=UniverseAudit.objects.all()

    context={
        "dataAuditUniverse":dataAuditUniverse,
    }

    return render(request, "./audit/subModuleCreateAudit.html", context)

def subModuleExectAudit(request):
    dataAudit=Audit.objects.all()
    dataUniverseAlias=UniverseAlias.objects.all()


    context={
        "dataAudit":dataAudit,
        "dataUniverseAlias":dataUniverseAlias
    }

    return render(request, "./audit/subModuleExectAudit.html", context)
#*********load to DataBase
def audit(request):
    # Esta vista permite interactuar con el submódulo "Crear Auditoría", para guardar una auditoria
    # en la base de datos, capturando los datos obtenidos desde el formulario.
    dataAuditUniverse=UniverseAudit.objects.all()
    dataAudit=Audit.objects.all()
    print("SI LLAMA A LA VISTA")
    
    # Se captura excepción para utilizar el caso inicial cuando la vista se llama desde el botón sin enviar parámetros 
    # a través del POST; es cuando action no se envía a través del POST.
    try:
        print("SI ENTRA AL TRY, PERO...")
        action=request.POST['action']
        typeAudit=request.POST['typeAudit'] 
        auditors=request.POST['auditors']
        zone=request.POST['zones']
        state=request.POST['state']
        city=request.POST['city'] 
        codeAudit=request.POST['codeAudit'] 
        ambient=request.POST['ambient']
        ambientDetail=request.POST['detailAmbient']
        datePlan=request.POST['datePlan']
        actDetail=request.POST['detailAct']
        idAudit="audit"+str(dataAudit.count())+"-"+codeAudit

        print("EL CÓDIGO ES:" +idAudit)
        

        context={
            
            "dataAuditUniverse":dataAuditUniverse,
            
        }
        # Desde el formulario se envía el parámetro action a través de una etiqueta input no visible, esto
        # permitirá usar una misma vista para varias acciones y se evitan crear tantas URL´s
        if action=="guardar":

            newAudit=Audit(
                typeAudit=typeAudit,
                auditor=auditors,
                zone=zone,
                state=state,
                city=city,
                codeAudit=codeAudit,
                ambient=ambient,
                ambientDetail=ambientDetail,
                datePlan=datePlan,
                actDetail=actDetail,
                idAudit=idAudit
                
            )

            newAudit.save()
            return render(request, "./audit/subModuleCreateAudit.html",context )

        else:
            return render(request, "./audit/subModuleCreateAudit.html", context)

    except Exception as e:
        print("AL PARECER HAY UN ERROR")
        print(e)
        context={
            "dataAuditUniverse":dataAuditUniverse,
            
        }
        return render(request, "./audit/subModuleCreateAudit.html",context)
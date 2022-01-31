from django.urls import path
from universe import views

urlpatterns = [
    #Queries
    path('listProcessUniverse/', views.listProcessUniverse, name='listProcessUniverse'),
    #Modules
    path('moduleUniverseAudit/',views.moduleUniverseAudit, name='moduleUniverseAudit'),
    #Submodules
    path('subModuleProcessUniverse/',views.subModuleProcessUniverse, name='subModuleProcessUniverse'),
    path('subModuleAuditUniverse/',views.subModuleAuditUniverse, name='subModuleAuditUniverse'),
    path('subModuleAliasUniverse/',views.subModuleAliasUniverse, name='subModuleAliasUniverse'),
    #load to DataBase
    path('auditUniverse/',views.auditUniverse, name='auditUniverse'),
    path('processUniverse/',views.processUniverse, name='processUniverse'),
    path('manageResponsableUniverse/',views.manageResponsableUniverse, name='manageResponsableUniverse'),
    path('macroProcessUniverse/',views.macroProcessUniverse, name='macroProcessUniverse'),
    # urls para las vistas prueba
    path('cargarPersona/',views.cargarPersona, name='cargarPersona'),
    path('prueba/',views.prueba),
    
]

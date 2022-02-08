from django.urls import path
from audit import views

urlpatterns = [
    path('',views.index, name='index'),
    #Queries
    path('listUniverse/', views.listUniverse, name='listUniverse'),
    #Modules
    #Submodules
    path('subModuleCreateAudit/', views.subModuleCreateAudit,name='subModuleCreateAudit'),

    #load to DataBase
    path('audit/', views.audit, name="audit"),
    
 
   
    
]

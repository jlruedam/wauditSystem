from django.urls import path
from audit import views

urlpatterns = [
    path('',views.index, name='index'),
    #Queries
    path('listUniverse/', views.listUniverse, name='listUniverse'),
    path('listAudit/', views.listAudit, name='listAudit'),
    #Modules
    #Submodules
    path('subModuleCreateAudit/', views.subModuleCreateAudit,name='subModuleCreateAudit'),
    path('subModuleExectAudit/', views.subModuleExectAudit,name='subModuleExectAudit'),
    

    #load to DataBase
    path('audit/', views.audit, name="audit"),
    
 
   
    
]

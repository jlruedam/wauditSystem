from django.urls import path
from universe import views

urlpatterns = [
    path('prueba/',views.prueba),
    path('universe/',views.universeAudit, name='universeAudit'),
    path('moduleProcessUniverse/',views.moduleProcessUniverse, name='moduleProcessUniverse'),
    path('processUniverse/',views.processUniverse, name='processUniverse'),
    path('manageResponsableUniverse/',views.manageResponsableUniverse, name='manageResponsableUniverse'),
    path('macroProcessUniverse/',views.macroProcessUniverse, name='macroProcessUniverse'),
    path('cargarPersona/',views.cargarPersona, name='cargarPersona')
]

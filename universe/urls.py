from django.urls import path
from universe import views

urlpatterns = [
    path('prueba/',views.prueba),
    path('universe/',views.universeAudit, name='universeAudit'),
    path('processUniverse/',views.processUniverse, name='processUniverse'),
    path('macroProcessUniverse/',views.macroProcessUniverse, name='macroProcessUniverse'),
    path('cargarPersona/',views.cargarPersona, name='cargarPersona')
]

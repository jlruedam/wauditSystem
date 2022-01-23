from django.shortcuts import render

# Create your views here.

def prueba(request):
    return render(request, "./universe/prueba.html")

def universeAudit(request):
    return render(request, "./universe/universeAudit.html")



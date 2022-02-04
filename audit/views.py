from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "./audit/index.html")

def subModuleCreateAudit(request):
    return render(request, "./audit/subModuleCreateAudit.html")
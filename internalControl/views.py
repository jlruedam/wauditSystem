from django.shortcuts import render

# Create your views here.

def moduleInternalControl(request):
    return render(request, "./internalControl/moduleInternalControl.html")

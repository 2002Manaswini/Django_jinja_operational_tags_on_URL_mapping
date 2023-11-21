from django.shortcuts import render

# Create your views here.
def bapi(request):
    return render(request,'bapi.html')

def babul(request):
    return render(request,'babul.html')
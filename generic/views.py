from django.shortcuts import render

# Create your views here.
def roshni(request):
    return render(request,'roshni.html')

def roshan(request):
    return render(request,'roshan.html')
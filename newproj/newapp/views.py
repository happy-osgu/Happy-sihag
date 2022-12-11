from django.shortcuts import render,HttpResponse
from .models import Service
# Create your views here.
def index(request):
    final=0
    try:
        num1=request.Get['name']
        num2=request.Get['email']
        num3=request.Get['phone']
        num4=request.Get['password']
        num5=request.Get['course']
        final=num1+num2+num3+num4+num5
        print(num1+num2+num3+num4+num5)

    except:
        pass
    return render(request,"contact.html",{'output':final})

def service(request):
    srs=Service.objects.all()
    context={
        "srs":srs
    }
    return render(request,"index.html",context)
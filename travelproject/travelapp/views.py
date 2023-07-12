from django.shortcuts import render
from .models import Place
from .models import People

def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})
def demo1(request)
    obj1=People.objects.all()
    return render(request,"index.html",{'result1':obj1})


from django.shortcuts import render
from .models import Place
from .models import People

def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})
def demo(request)
    obj=People.objects.all()
    return render(request,"index.html",{'result':obj})


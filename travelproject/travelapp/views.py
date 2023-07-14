from django.shortcuts import render
from .models import Place
from .models import Peoples

def demo(request):
    obj=Place.objects.all()
    obj1=Peoples.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

from django.shortcuts import render


def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result:obj})

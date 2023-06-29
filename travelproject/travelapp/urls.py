from . import views
from django.urls import path, include

urlpatterns = [path('',views.demo,name='travelapp'),
               # path('about/',views.about,name='about')
               ]

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path("",views.index,name='myapp'),
   path("about",views.index,name='about'),
   path("services",views.index,name='myapp')
]
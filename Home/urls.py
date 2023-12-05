from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [    
    path("",views.index, name='Home'),
    path("home",views.home, name='home'),
    path("availabletest",views.availabletest, name='availabletest'),
    path("package",views.package, name='package'),
    path("report",views.report, name='report'),
    path("feedback",views.feedback, name='feedback')
]
 
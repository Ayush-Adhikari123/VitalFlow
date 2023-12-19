from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path("",views.index,name='myapp'),
   path("about",views.about,name='about'),
   path("services",views.index,name='myapp'),
   path("home",views.home, name='home'),
   path("availabletest",views.availabletest, name='availabletest'),
   path("package",views.package, name='package'),
   path("report",views.report, name='report'),
   path("feedback",views.feedback, name='feedback'),
   path("contact",views.contact, name='contact'),
   path("adminpage",views.adminpage, name='adminpage'),
   path("adminlogin",views.adminlogin, name='adminlogin'),
   path("viewreport",views.viewreport,name='viewreport'),
   path("createreport",views.createreport,name='createreport'),
   path("test",views.test,name='test')
]
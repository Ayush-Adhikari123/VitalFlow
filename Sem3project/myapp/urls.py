# urls.py
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
   path("adminprofile",views.adminprofile, name='adminprofile'),
   path("createreport",views.createreport,name='createreport'),
    path("techlogin",views.techlogin, name='techlogin'),
    path("packages",views.packages, name='packages'),
 path("viewreport",views.viewreport,name='viewreport'),
 ]
<<<<<<< HEAD
# urls.py
=======
>>>>>>> origin/pradip
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
<<<<<<< HEAD
   # path("adminprofile",views.adminprofile, name='adminprofile'),
   path("createreport",views.createreport,name='createreport'),
      path("createtechnicianlogin",views.createtechnicianlogin,name='createtechnicianlogin'),
    path("packages",views.packages, name='packages'),
 path("viewreport",views.viewreport,name='viewreport'),

#  path("adminlogin",views.adminlogin,name='adminlogin'),
path('adminlogin/',views.admin_login,name ='adminlogin'),
path('adminlogout/',views.admin_logout,name ='adminlogout'),
path('adminprofile/',views.admin_profile,name='adminprofile'),
path('changepassword/',views.admin_password,name='changepassword'),

path("techadd/",views.techadd,name='techadd'),


path("updatereport/<str:contact>/",views.updatereport,name='updatereport'),
=======
   path("adminpage",views.adminpage, name='adminpage'),
   path("createreport",views.createreport,name='createreport'),
   path("createtechnicianlogin",views.createtechnicianlogin,name='createtechnicianlogin'),
   path("createadminpage",views.createadminpage,name="createadminpage"),
   path("createuserlogin",views.createuserlogin,name="createuserlogin")
   

>>>>>>> origin/pradip
 ]
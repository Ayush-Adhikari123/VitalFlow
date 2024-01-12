# urls.py
from django.contrib import admin
from django.urls import path
from myapp import views

from django.contrib.auth import views as auth_views 


urlpatterns = [
   path("",views.index,name='myapp'),
   path("about",views.about,name='about'),
   path("services",views.index,name='myapp'),
   path("home",views.home, name='home'),
   path("availabletest",views.availabletest, name='availabletest'),
   path("feedback",views.feedback, name='feedback'),
   path("contact",views.contact, name='contact'),
   path("createreport",views.createreport,name='createreport'),
   path("techlogin",views.techlogin,name='techlogin'),
   path("packages",views.packages, name='packages'),
   path("viewreport",views.viewreport,name='viewreport'),
   path('adminlogin/',views.admin_login,name ='adminlogin'),
   path('adminlogout/',views.admin_logout,name ='adminlogout'),
   path('adminprofile/',views.admin_profile,name='adminprofile'),
   path('changepassword/',views.admin_password,name='changepassword'),
   path('techprofile',views.techprofile,name='techprofile'),
   path("updatereport/<str:contact>/",views.updatereport,name='updatereport'),
   path("techadd",views.techadd,name='techadd'),
   path("techpannel",views.techpannel,name='techpannel'),
# -------------------------------------------------------------------------------
   path('password_reset/',auth_views.PasswordResetView.as_view(template_name='passwordreset.html'),name='password_reset'),
   path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='resetdone.html'),name='password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
   path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='resetcomplete.html'),name='password_reset_complete'),
   
# -------------------------------------------------------------------------------
   path('passwordreset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='passwordreset'),
   path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='newpassword.html'),name='password_reset_confirm'),
   


path("updatereport/<str:contact>/",views.updatereport,name='updatereport'),
path("gethomeservice",views.book_service,name='updatereport'),
path('book', views.book_home_service, name='book_service'),

   path("homeservicepannel",views.homeservicepannel,name='homeservicepannel'),
   path("userlogin",views.userlogin,name='userlogin'),
   path('test',views.test, name='test'),
   path('diagnostic',views.diagnostic, name='diagnostic'),
   path("contactpannel",views.contactpannel,name='contactpannel'),
   path('delete/<int:record_id>/', views.delete_record, name='delete_record'),
 ]

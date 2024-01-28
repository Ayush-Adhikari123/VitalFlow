# urls.py
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from myapp import views

urlpatterns = [
   path("",views.index,name='myapp'),
   path("home",views.index,name='myapp'),
   path("availabletest",views.availabletest, name='availabletest'),
   path("feedback",views.feedback, name='feedback'),
   path("contact",views.contact, name='contact'),
   path("createreport",views.createreport,name='createreport'),
   path("techlogin",views.techlogin,name='techlogin'),
   path("viewreport",views.viewreport,name='viewreport'),
   path('adminlogin/',views.admin_login,name ='adminlogin'),
   path('adminlogout/',views.admin_logout,name ='adminlogout'),
   path('adminprofile/',views.admin_profile,name='adminprofile'),
   path('changepassword/',views.admin_password,name='changepassword'),
   path('techprofile',views.techprofile,name='techprofile'),
   path("updatereport/<str:contact>/",views.updatereport,name='updatereport'),
   path("techadd",views.techadd,name='techadd'),
   path("techpannel",views.techpannel,name='techpannel'),
   path('deletetech/<int:record_id>/', views.delete_techrecord, name='delete_techrecord'),
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
   path('update_done_status/<int:service_id>/<str:tempmail>/', views.update_done_status, name='update_done_status'),
   path('delete_service/<int:service_id>/', views.delete_service, name='delete_service'),
   path("userlogin",views.userlogin,name='userlogin'),
   path('test',views.test, name='test'),
   path("contactpannel",views.contactpannel,name='contactpannel'),
   path('delete/<int:record_id>/', views.delete_record, name='delete_record'),
   path('feedbackpannel',views.feedbackpannel, name='feedback'),
   path('delete_feed/<int:feed_id>/', views.delete_feed, name='delete_feedback'),
   path('hide_feed/<int:feed_id>/', views.hide_feedback, name='hide_feedback'),
   path('show_feed/<int:feed_id>/', views.show_feedback, name='hide_feedback'),
   path("feedback",views.feedback, name='feedback'),
 ]


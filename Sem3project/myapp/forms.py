#forms.py
from django import forms
from .models import Report_Detail  # Import your ReportDetail model here

class Report_DetailForm(forms.ModelForm):
    class Meta:
        model = Report_Detail  # Replace ReportDetail with your model name
        fields = ['test_list']

        # fields=['test_list']# Include all fields or specify the fields you need

<<<<<<< HEAD
class PatientForm(forms.Form):

    patient_Name = forms.CharField(max_length=255)
    contact = forms.CharField(max_length=15)
=======

>>>>>>> 7def4dbffb9783ceda45eccbb1b5c2d772b39176
# =============================================suvam ko part

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class EditadminprofileForm(UserChangeForm):
    password=None
    class Meta:
        model =User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels={'email': 'Email' }


class EditsuperadminprofileForm(UserChangeForm):
    password=None
    class Meta:
        model =User
        fields = '__all__'
        labels={'email': 'Email' }

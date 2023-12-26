#forms.py
from django import forms
from .models import Report_Detail  # Import your ReportDetail model here
from .models import Report

class Report_DetailForm(forms.ModelForm):
    class Meta:
        model = Report_Detail  # Replace ReportDetail with your model name
        fields = ['test_list']

        # fields=['test_list']# Include all fields or specify the fields you need
class PatientForm(forms.Form):

    patient_Name = forms.CharField(max_length=255)
    contact = forms.CharField(max_length=15)
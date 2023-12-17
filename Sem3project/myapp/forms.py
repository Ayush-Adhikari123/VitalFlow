#forms.py
from django import forms
from .models import Report_Detail  # Import your ReportDetail model here

class Report_DetailForm(forms.ModelForm):
    class Meta:
        model = Report_Detail  # Replace ReportDetail with your model name
        fields = ['test_list']

        # fields=['test_list']# Include all fields or specify the fields you need

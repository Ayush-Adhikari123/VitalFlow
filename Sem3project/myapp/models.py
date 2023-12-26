# models.py
from django.db import models

# Create your models here.
class Report(models.Model): 
    patient_Name =models.CharField( max_length=50)
    age=models.IntegerField()
    gender=models.CharField( max_length=50)
    address =models.CharField( max_length=50)
    lab_no =models.IntegerField( )
    contact =models.IntegerField( )   
    date =models.DateField( max_length=50)
    consultant =models.CharField( max_length=50)
    
class Report_Detail(models.Model):
    test_list =models.CharField( max_length=50)
    investigation =models.CharField( max_length=50)
    results =models.CharField( max_length=50)
    reference_value =models.CharField( max_length=50)
    unit =models.CharField( max_length=50)
    report=models.ForeignKey(Report, null=True,blank=True, on_delete=models.CASCADE)
    
    

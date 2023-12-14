from django.db import models

# Create your models here.
class Report(models.Model):
    patient_Name =models.CharField( max_length=50)
    dispatch_date =models.CharField( max_length=50)
    age=models.IntegerField()
    gender=models.CharField( max_length=50)
    address =models.CharField( max_length=50)
    lab_no =models.IntegerField( )
    contact =models.IntegerField( )
    date =models.CharField( max_length=50)
    consultant =models.CharField( max_length=50)
    investigation =models.CharField( max_length=50)
    results =models.CharField( max_length=50)
    reference_value =models.CharField( max_length=50)
    unit =models.CharField( max_length=50)
    

class technicianlogin(models.Model):
    technician_id=models.CharField(max_length=32)
    Password=models.CharField(max_length=16)

class adminpage(models.Model):
    admin_id=models.CharField(max_length=32)
    Password=models.CharField(max_length=16)

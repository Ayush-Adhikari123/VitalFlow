<<<<<<< HEAD
# models.py
=======
>>>>>>> origin/pradip
from django.db import models

# Create your models here.
class Report(models.Model):
    patient_Name =models.CharField( max_length=50)
<<<<<<< HEAD
=======
    dispatch_date =models.CharField( max_length=50)
>>>>>>> origin/pradip
    age=models.IntegerField()
    gender=models.CharField( max_length=50)
    address =models.CharField( max_length=50)
    lab_no =models.IntegerField( )
<<<<<<< HEAD
    contact =models.IntegerField( )   
    date =models.DateField( max_length=50)
    consultant =models.CharField( max_length=50)
    
class Report_Detail(models.Model):
    test_list =models.CharField( max_length=50)
=======
    contact =models.IntegerField( )
    date =models.CharField( max_length=50)
    consultant =models.CharField( max_length=50)
>>>>>>> origin/pradip
    investigation =models.CharField( max_length=50)
    results =models.CharField( max_length=50)
    reference_value =models.CharField( max_length=50)
    unit =models.CharField( max_length=50)
<<<<<<< HEAD
    report = models.ForeignKey(Report, blank=True, null=True, on_delete=models.CASCADE)
    
class technicianlogin(models.Model):
    technician_id=models.CharField(max_length=32)
    Password=models.CharField(max_length=16)    
=======
    

class technicianlogin(models.Model):
    technician_id=models.CharField(max_length=32)
    Password=models.CharField(max_length=16)

class adminpage(models.Model):
    admin_id=models.CharField(max_length=32)
    Password=models.CharField(max_length=16)

class userlogin(models.Model):
    user_id=models.CharField(max_length=10)
    user_contact=models.CharField(max_length=32)




>>>>>>> origin/pradip

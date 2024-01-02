# models.py
from django.db import models
from django.contrib.auth.models import User

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
    report = models.ForeignKey(Report, blank=True, null=True, on_delete=models.CASCADE)
    
class technicianlogin(models.Model):
    technician_id=models.CharField(max_length=32)
    Password=models.CharField(max_length=16)   
    
class TechAdd(models.Model):
    first_name =models.CharField( max_length=50)
    middle_name=models.CharField( max_length=50,null=True)
    last_name=models.CharField( max_length=50)    
    email =models.EmailField(null=True)
    contact =models.IntegerField( )
    password=models.CharField(max_length=50)
    com_password=models.CharField(max_length=50)        
    gender =models.CharField( max_length=50)



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username    
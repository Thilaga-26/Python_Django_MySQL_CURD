from django.db import models

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=100) 
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) 
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
    address = models.CharField(max_length=255)
   
    class Meta:  
        db_table = "Employee_Table"

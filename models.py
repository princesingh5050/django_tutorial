from django.db import models

# Create your models here.
class Account(models.Model):
    userid=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    mobile=models.CharField(max_length=10)
    type=models.CharField(max_length=10)
    class Meta:
        db_table='account'

class student(models.Model):
    studentid = models.CharField(max_length=20, unique=True)
    student_password = models.CharField(max_length=20)
    student_name = models.CharField(max_length=20)
    student_fname = models.CharField(max_length=10)
    student_email= models.CharField(max_length=40)
    student_mobile = models.CharField(max_length=10)
    class Meta:
        db_table='student'


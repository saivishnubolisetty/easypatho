from django.db import models

# Create your models here.

class ccpr(models.Model):
    Name=models.CharField(max_length=20)
    CompanyName= models.CharField(max_length=20)
    EmployeeStrength= models.IntegerField(null=True)
    phone=models.IntegerField(null=False,default=False)
    Email=models.EmailField()
    city=models.CharField(max_length=20)
    message = models.TextField(null=True)

class sup(models.Model):
    uid=models.PositiveIntegerField()
    username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)

class register(models.Model):
    name=models.CharField(max_length=20,null=False)
    pack=models.CharField(max_length=20,null=True)
    service=models.CharField(max_length=20,null=True)
    test=models.CharField(max_length=20,null=True)
    mail=models.EmailField(null=True)
    std=models.CharField(max_length=10,null=False)
    phone = models.IntegerField(null=False)
    month=models.CharField(max_length=10,null=False)
    day=models.CharField(max_length=10,null=False)
    year=models.CharField(max_length=10,null=False)
    gender=models.CharField(max_length=10, null=False)
    date=models.CharField(max_length=10)
    time=models.CharField(max_length=5)
    country=models.CharField(max_length=30)

class emp(models.Model):
    empname=models.CharField(max_length=20,null=False)
    password=models.CharField(max_length=20,null=False)

def __str__(self):
    return self.Name


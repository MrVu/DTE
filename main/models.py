from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime 

# Create your models here.
class SaleSummary(models.Model):
    class Meta:
        verbose_name = 'Sale Summary'
        verbose_name_plural = 'Sales Summary'

class Customer(models.Model):
    fullName= models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    phoneNumber = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    ielts = models.FloatField(null=True)
    budget = models.BigIntegerField(null=True)
    currentJob = models.CharField(max_length=200, null=True)
    education = models.IntegerField(null=True)
    status = models.CharField(max_length=200, null=True, choices=[('Contact', 'Contact'),('Pending', 'Pending'),('Done','Done')])
    exp = models.IntegerField(null=True)
    description=models.TextField(blank=True)
    profilePic = models.ImageField()
    def __str__(self):
        return self.fullName

class JobAvailable(models.Model):
    country = models.CharField(max_length=200, null=True)
    ielts = models.IntegerField(null=True)
    city = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    minExp = models.IntegerField(null=True)
    education = models.IntegerField(null=True)
    budget = models.BigIntegerField(null=True)
    available = models.IntegerField(null=True)
    def __str__(self):
        return self.position

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=20, blank=True, choices=[('Consultant', 'Consultant'),('Sale', 'Sale'), ('Manager', 'Manager')])
    profilePic = models.ImageField(null=True)

class Tracking(models.Model):
    userName = models.CharField(max_length=50)
    request = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.userName

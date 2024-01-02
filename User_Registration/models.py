from django.db import models

# Create your models here.
class User_registration(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email_address=models.EmailField(max_length=30,unique=True)
    phone_number=models.CharField(max_length=12,unique=True)
    place=models.CharField(max_length=50)
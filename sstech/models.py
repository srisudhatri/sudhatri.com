from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phoneNumber=models.IntegerField()
    message=models.TextField()
    

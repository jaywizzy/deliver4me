from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DispatchRider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True) 
    phone_number = models.CharField(max_length=20, null=True) 
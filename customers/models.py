from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True) 
    phone_number = models.CharField(max_length=20, null=True) 


# @receiver(post_save, sender=User)
# def create_customer(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_customer(sender, instance, **kwargs):
#     instance.customer.save()
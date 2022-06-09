from django.db import models
from customers.models import *
from riders.models import *

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pickup_address = models.TextField(null=True)
    delivery_address = models.TextField(null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    dispatch_rider = models.ForeignKey(DispatchRider, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now=True)


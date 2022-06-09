from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(DispatchRider)
class DispatchRiderAdmin(admin.ModelAdmin):
    pass
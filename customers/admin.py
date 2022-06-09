from django.contrib import admin
from .models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    # pass
    list_display = ('user', 'address', 'phone_number')


admin.site.register(Customer, CustomerAdmin)


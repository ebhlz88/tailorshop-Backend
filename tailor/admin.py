from django.contrib import admin
from .models import order,customer
# Register your models here.
admin.site.register(customer)
admin.site.register(order)
from django.contrib import admin
from . models import Products, Categories, Brand,Customer,Cart
# Register your models here.
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Customer)
admin.site.register(Cart)
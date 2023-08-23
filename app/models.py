from typing import Any
from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=250,null=True)
    description = models.CharField(max_length=500,null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='productImages',null=True)
    sale_price = models.FloatField(null=True)
    discounted_price = models.FloatField(null=True)
    time_gram = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
    

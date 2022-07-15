from distutils.command.upload import upload
from pyexpat import model
from unicodedata import name
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=0)
    image = models.ImageField(upload_to='shop/product/%Y/%m/%d/')
    discount = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.product_name

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

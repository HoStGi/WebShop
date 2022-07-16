from django.db import models
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('show_product', kwargs={'product_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('show_category', kwargs={'cat_id': self.pk})

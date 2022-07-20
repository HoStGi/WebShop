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

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone = models.CharField(unique=True, max_length=12,)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
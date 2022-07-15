from django.shortcuts import render
from .models import Product, Category
def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'product': products})


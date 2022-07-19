from django.shortcuts import get_object_or_404, render
from .models import Product, Category


def home(request):
    products = Product.objects.filter(published=True)
    cats = Category.objects.all()  
    return render(request, 'shop/home.html', {'products': products, 'cats':cats, 'cat_selected': 0})

def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'GET':
        return render(request, 'shop/show_product.html', {'product': product})

def show_category(request, cat_id):
    products = Product.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    return render(request, 'shop/home.html', {'products': products, 'cats':cats, 'cat_selected':cat_id})
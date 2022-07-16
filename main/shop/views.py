from django.http import Http404, HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Product, Category
from .forms import ProductForm


def home(request):
    products = Product.objects.all()
    cats = Category.objects.all()  
    return render(request, 'shop/home.html', {'products': products, 'cats':cats, 'cat_selected': 0})

def productdetail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'GET':
        return render(request, 'shop/productview.html', {'product': product})

def show_category(request, cat_id):
    products = Product.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    return render(request, 'shop/home.html', {'products': products, 'cats':cats, 'cat_selected':cat_id})
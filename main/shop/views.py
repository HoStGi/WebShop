from django.shortcuts import get_object_or_404, render
from .models import Product, OrderItem, Order, Category
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm, OrderCreateForm



def home(request):
    products = Product.objects.filter(published=True)
    cats = Category.objects.all()  
    return render(request, 'shop/home.html', {'products': products, 'cats':cats, 'cat_selected': 0})

def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_product_form = CartAddProductForm()
    if request.method == 'GET':
        return render(request, 'shop/show_product.html', {'product': product, 
        'cart_product_form': cart_product_form})

def show_category(request, cat_id):
    products = Product.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    return render(request, 'shop/home.html', {'products': products, 'cats':cats, 'cat_selected':cat_id})

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'shop/cart_detail.html', {'cart': cart})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'shop/order_created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'shop/order_create.html', {'cart':cart, 'form':form})
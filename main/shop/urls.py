from django.urls import path
from .views import home, order_create, show_product, show_category, cart_add, cart_detail, cart_remove


urlpatterns = [
  path('', home, name='home'),
  path('product/<int:product_id>', show_product, name='show_product'),
  path('category/<int:cat_id>', show_category, name='show_category'),
  
  path('cart/', cart_detail, name='cart_detail'),
  path('add/<int:product_id>/', cart_add, name='cart_add'),
  path('remove/<int:product_id>/',cart_remove,name='cart_remove'),

  path('order_create/', order_create, name='order_create'),
]

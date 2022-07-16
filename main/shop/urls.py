from django.urls import path
from .views import home, show_product, show_category

urlpatterns = [
  path('', home, name='home'),
  path('product/<int:product_id>', show_product, name='show_product'),
  path('category/<int:cat_id>', show_category, name='show_category'),
]

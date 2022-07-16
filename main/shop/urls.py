from django.urls import path
from .views import home, productdetail, show_category

urlpatterns = [
  path('', home, name='home'),
  path('<int:product_id>', productdetail, name='productdetail'),
  path('category/<int:cat_id>', show_category, name='show_category'),
]

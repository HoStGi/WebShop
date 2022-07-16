from django.urls import path
from .views import logoutuser, register, login_view

urlpatterns = [
    path('signupuser/', register, name='signupuser'),
    path('loginuser/', login_view, name='loginuser'),
    path('logoutuser/', logoutuser, name='logoutuser'),
]

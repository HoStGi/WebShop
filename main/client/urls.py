from django.urls import path, include
from .views import signupuser, loginuser, SignUp, logoutuser, register, login, login_view

urlpatterns = [
    path('signupuser/', register, name='signupuser'),
    path('loginuser/', login_view, name='loginuser'),
    path('logoutuser/', logoutuser, name='logoutuser'),
    path('login/', include('django.contrib.auth.urls')),
]

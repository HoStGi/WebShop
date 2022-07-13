from django.urls import path
from .views import signupuser, loginuser

urlpatterns = [
    path('signupuser/', signupuser, name='signupuser'),
    path('loginuser/', loginuser, name='loginuser'),
]

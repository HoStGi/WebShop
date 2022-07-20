from django import forms
from django.forms import ModelForm, Form, TypedChoiceField, BooleanField, HiddenInput
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'phone']

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(Form):
    quantity = TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = BooleanField(required=False, initial=False, widget=HiddenInput)



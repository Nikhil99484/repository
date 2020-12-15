from  django import forms
from .models import Orders,Customers,Products
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=['customer','product','status']

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customers
        fields=['name','email','mobile']
class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields='__all__'

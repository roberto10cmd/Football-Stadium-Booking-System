from django.forms import ModelForm
from .models import Order, Stadium, Equipment,Customer
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class CreateUseForm(UserCreationForm):
    firstname = forms.CharField(max_length=255, required=True)
    lastname = forms.CharField(max_length=255, required=True)
    address = forms.CharField(max_length=255, required=False)
    phone = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'firstname', 'lastname', 'address', 'phone']

class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = ['name', 'location', 'description']

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'description']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
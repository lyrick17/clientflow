from django.forms import ModelForm
from .models import Order
from django.contrib.auth.forms import UserCreationForm  #
from django.contrib.auth.models import User
from django import forms



class OrderForm(ModelForm):
    class Meta:
        model = Order       # needs to know which model we going to build form for
        fields = '__all__'  # create form with all fields in, if selected fields, create list instead

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
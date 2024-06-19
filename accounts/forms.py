from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order       # needs to know which model we going to build form for
        fields = '__all__'  # create form with all fields in, if selected fields, create list instead

    
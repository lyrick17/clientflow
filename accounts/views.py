from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import OrderForm
# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count() # count amount of data in customers
    total_orders = orders.count()       # count amount of data in orders
    delivered = orders.filter(status='Delivered').count() # filter delivers
    pending = orders.filter(status='Pending').count() # filter delivers

    context = {"orders": orders, 
               "customers": customers,
               "total_customers": total_customers,
               "total_orders": total_orders,
               "delivered": delivered,
               "pending": pending}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    
    products = Product.objects.all() # query into db to get all products

    context = {"products": products}
    return render(request, 'accounts/products.html', context)

def customer(request, primary_key):

    customer = Customer.objects.get(id=primary_key)

    orders = customer.order_set.all()
    order_count = orders.count()
    context = {"customer": customer, 
               "orders": orders, 
               "order_count": order_count}
    return render(request, 'accounts/customer.html', context)

# CRUD Operations for Orders
def createOrder(request):
    form = OrderForm()

    # once form is submitted, it will call this method, then check if post request has been made
    if request.method == "POST":
        # debugging purposes
        # print('Printing POST:', request.POST)
        
        # process and save the form
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to home page
            return redirect('/')
        
    context = {"form": form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, primary_key):
    
    order = Order.objects.get(id=primary_key)
    form = OrderForm(instance=order)


    if request.method == "POST":
        # process and update the form
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            # redirect to home page
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)
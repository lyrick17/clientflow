from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory  # basically way of creating multiple forms in one form
from django.core.paginator import Paginator     # pagination

from .models import *
from .forms import OrderForm
from .filters import OrderFilter

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
    
    products_list = Product.objects.all()            # query into db to get all products

    paginator = Paginator(products_list, 5)    # show 10 products per page

    page_num = request.GET.get('page')
    products_display = paginator.get_page(page_num)


    context = {"products": products_display}
    return render(request, 'accounts/products.html', context)

def customer(request, primary_key):

    customer = Customer.objects.get(id=primary_key)

    orders = customer.order_set.all()
    order_count = orders.count()
    
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {"customer": customer, 
               "orders": orders, 
               "order_count": order_count,
               'myFilter': myFilter}
    return render(request, 'accounts/customer.html', context)

# CRUD Operations for Orders
def createOrder(request, customer_key):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=customer_key)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer': customer})
    print(customer)
    # once form is submitted, it will call this method, then check if post request has been made
    if request.method == "POST":
        # debugging purposes
        # print('Printing POST:', request.POST)
        
        # process and save the form
        formset = OrderFormSet(request.POST, instance=customer)
        #form = OrderForm(request.POST)
        if formset.is_valid():
            formset.save()
            # redirect to home page
            return redirect('/')
        
    context = {"formset": formset}
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

def deleteOrder(request, primary_key):
    order = Order.objects.get(id=primary_key)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
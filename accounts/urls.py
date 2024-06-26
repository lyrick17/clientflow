from django.urls import path
from . import views

# <str:____> is django's way  of making url clicking dynamic 
# name= is important to not affect the callings from other templates even if you update the url path
urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:primary_key>', views.customer, name="customer"),

    path('create_order/<str:customer_key>', views.createOrder, name="create_order"), # key of customer
    path('update_order/<str:primary_key>', views.updateOrder, name="update_order"), # key of order
    path('delete_order/<str:primary_key>', views.deleteOrder, name="delete_order")  # key of order

]

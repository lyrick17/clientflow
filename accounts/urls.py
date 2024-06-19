from django.urls import path
from . import views

# <str:____> is django's way  of making url clicking dynamic 
# name= is important to not affect the callings from other templates even if you update the url path
urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:primary_key>', views.customer, name="customer"),

    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:primary_key>', views.updateOrder, name="update_order")
]

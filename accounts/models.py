from django.db import models

# Create your models here.

class Customer(models.Model):
    # name, phone, email, date_created
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    # name 
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    # name, price, category, description, date_created, tags

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)

    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    # date_created, status
    

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    

    def __str__(self):
        return self.product.name
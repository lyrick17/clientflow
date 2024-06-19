#(1) Returns all  customers from customer table
customers = Customer.objects.all()

#(2) Returns first customer in table
firstCustomer =  Customer.objects.first()

#(3) returns last customer in table
lastCustomer = Customer.objects.last()

#(4) Returns single customer by name
customerByName  =  Customer.objects.get(name='Kafka')

#(5) Returns single customer by id
customerById = Customer.objects.get(id=4)

#(6) Returns all orders related to customer (firstCustomer variable set above)
firstCustomer.order_set.all()

#(7) Retuns orders customer name: (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

#(8) Returns products from products table with value of "Outdoor"
products = Product.objects.filter(category="Outdoor")

#(9) Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

#(10) Returns all products with tag of "Sports": (Query Many to Many)
productsFiltered = Product.objects.filter(tags__name="Sports")


# Returns the total count for number of time a ball was ordered by  the first customer
ballOrders = firstcustomer.order_set.filter(product__name="Ball").count()

allOrders = {}

for order in firstCustomer.order_set.all():
    if  order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1
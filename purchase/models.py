from django.db import models


class Customer(models.Model):
    """
        Table of customers.

    """

    name = models.CharField(max_length = 256)
    gender = models.CharField(max_length = 1)
    age = models.SmallIntegerField()
    last_buy = models.DateTimeField(auto_created = True, auto_now = True)
    first_buy = models.DateTimeField(auto_created = True, auto_now = False)

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'Name: ' + str(self.name) \
                + ' ' + 'Gender: ' + str(self.gender)


class Order(models.Model):
    """
        Table of orders

    """
    customer = models.ForeignKey('Customer', on_delete = models.CASCADE, null = False, default = None)
    employee = models.ForeignKey('trade_point.Employee', on_delete = models.CASCADE, null = False, default = None)
    counter = models.ForeignKey('trade_point.Counter', on_delete = models.CASCADE, null = False, default = None)
    date = models.DateField(auto_created = True)

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'Customer: ' + str(self.customer.name) \
                + ' ' + 'Employee: ' + str(self.employee.name) + ' ' + str(self.date)


class OrderDetails(models.Model):
    """
        Table with details of purchases

    """
    order = models.ForeignKey('Order', on_delete = models.CASCADE, default=None)
    product = models.ForeignKey('product.Product', on_delete = models.CASCADE, default=None)
    quantity = models.SmallIntegerField()
    price = models.FloatField()

    def __str__(self):
        return 'Order: ' + str(self.order.id) + ' ' + 'Product: ' + str(self.product.name) \
                + ' ' + 'Quantity: ' + str(self.quantity) + ' ' + 'Price: ' + str(self.price)



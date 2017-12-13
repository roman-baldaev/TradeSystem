from django.db import models


class Supplier(models.Model):
    """
        Table of suppliers.

    """

    name = models.CharField(max_length = 256)
    activity = models.CharField(max_length = 1)
    delays = models.SmallIntegerField()

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'Name: ' + str(self.name) \
                + ' ' + 'Activity: ' + str(self.activity) + ' ' + 'Delays: ' + str(self.delays)


class Delivery(models.Model):
    """
        Delivery table

    """
    request = models.ForeignKey('request.ManagerRequest', on_delete = models.CASCADE, null = False, default = None)
    date = models.DateTimeField(auto_created = True, auto_now = False)

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'Manager: ' + str(self.request.employee.name) \
                      + ' ' + 'Supplier: ' + str(self.request.supplier.name) + ' ' + 'Date: ' \
                      + str(self.date)


class DeliveryDetails(models.Model):
    """
        More information about delivery

    """
    delivery = models.ForeignKey('Delivery', on_delete = models.CASCADE, null = False, default = None)
    request_details = models.ForeignKey('request.ManagerRequestDetails', on_delete = models.CASCADE, null = False,
                                        default = None)
    price = models.FloatField()

    def __str__(self):
        return  'id: ' + str(self.id) + ' ' + 'Product: ' + str(self.request_details.product.name) + \
                ' ' + 'Quantity: ' + str(self.request_details.quantity)
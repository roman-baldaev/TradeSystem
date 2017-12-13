from django.db import models


class TradePointRequest(models.Model):
    """
        Requests from trade points to company managers.

    """

    manager_request = models.ForeignKey('ManagerRequest', on_delete = models.CASCADE,
                                    null = False, default = None)
    trade_point = models.ForeignKey('trade_point.TradePoint', on_delete = models.CASCADE,
                                    null = False, default = None)
    date = models.DateTimeField(auto_now = False, auto_created = True)

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'Trade point: ' + str(self.trade_point.name) \
                + ' ' + 'Date: ' + str(self.date)


class TradePointRequestDetails(models.Model):
    """
        More information about trade point request.

    """
    request = models.ForeignKey('TradePointRequest', on_delete = models.CASCADE, null = False, default = None)
    product = models.ForeignKey('product.Product', on_delete = models.CASCADE, null = False, default = None)
    quantity = models.IntegerField()

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'Trade point: ' + str(self.request.trade_point.name) \
                      + ' ' + 'Product: ' + str(self.product.name) + ' ' + 'Quantity: ' \
                      + str(self.quantity)


class ManagerRequest(models.Model):
    """
        Processed requests from trade points addressed directly to suppliers.

    """
    employee = models.ForeignKey('trade_point.Employee', on_delete = models.CASCADE, null = False, default = None)
    request = models.ForeignKey('TradePointRequest', on_delete = models.CASCADE, null = False, default = None)
    date = models.DateTimeField(auto_now = False, auto_created = True)
    end_date = models.DateTimeField(auto_now=False, auto_created=True)
    supplier = models.ForeignKey('delivery.Supplier', on_delete = models.CASCADE, null = False, default = None)

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'Trade point: ' + str(self.request.trade_point.name) \
                + ' ' + 'Date: ' + str(self.date) + ' ' + 'End date: ' + str(self.end_date)


class ManagerRequestDetails(models.Model):
    """
        More information about manager request.

    """
    request = models.ForeignKey('ManagerRequest', on_delete = models.CASCADE, null = False, default = None)
    product = models.ForeignKey('product.Product', on_delete = models.CASCADE, null = False, default = None)
    quantity = models.IntegerField()

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'Trade point: ' + str(self.request.request.trade_point.name) \
                      + ' ' + 'Product: ' + str(self.product.name) + ' ' + 'Quantity: ' \
                      + str(self.quantity)

from django.db import models


class Product(models.Model):
    """
        Table of products.

    """

    name = models.CharField(max_length = 256)
    description = models.TextField(null = True)

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'Name: ' + str(self.name) \
                + ' ' + 'Description: ' + str(self.description)


class Stock(models.Model):
    """
        Merchandise table

    """
    trade_point = models.ForeignKey('trade_point.TradePoint', on_delete = models.CASCADE, null = False, default = None)
    product = models.ForeignKey('Product', on_delete = models.CASCADE, null = False, default = None)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'Trade point: ' + str(self.trade_point.name) \
                + ' ' + 'Product: ' + str(self.product.name) + ' ' + 'Quantity: ' + str(self.quantity) \
                + ' ' + 'Price: ' + str(self.price)



from django.db import models


class TradePoint(models.Model):
    """
        Table of trade points.
    """

    name = models.CharField(max_length = 256)
    type = models.SmallIntegerField()

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'Name: ' + str(self.name) \
                + ' ' + 'Type: ' + str(self.type)


class Workshop(models.Model):
    """
        Table of workshops - sections of trade points
    """
    trade_point = models.ForeignKey('TradePoint', on_delete = models.CASCADE, null = False, default = None)
    chief = models.ForeignKey('Employee', on_delete = models.CASCADE, null = True, default = None, related_name="Chief")

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'TP_id: ' + str(self.trade_point) \
                + ' ' + 'Chief: ' + str(self.chief)


class Area(models.Model):
    """
        Table of information about area of trade point
    """

    workshop = models.ForeignKey('Workshop', on_delete = models.CASCADE, default=None)
    value = models.FloatField()
    date_to_end = models.DateField()
    cost = models.FloatField()
    def __str__(self):
        return 'Workshop: ' + str(self.workshop) + ' ' + 'Value: ' + str(self.value) \
                + ' ' + 'Cost: ' + str(self.cost)


class Utilities(models.Model):
    """
        History of utility payments
    """
    workshop = models.ForeignKey('Workshop', on_delete=models.CASCADE, default=None)
    date = models.DateField()
    cost = models.FloatField()

    def __str__(self):
        return 'Workshop: ' + str(self.workshop) + ' ' + 'Date: ' + str(self.date) \
            + ' ' + 'Cost: ' + str(self.cost)


class Counter(models.Model):
    """
        Information about counters
    """
    workshop = models.ForeignKey('Workshop', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return 'id: ' + str(self.id) + ' ' + 'Workshop: ' + str(self.workshop)


class Employee(models.Model):
    """
        Information about employees
    """

    name = models.CharField(max_length = 256)
    workshop = models.ForeignKey('Workshop', on_delete = models.CASCADE, default = None, null = True)
    start_date = models.DateField(auto_now = False)
    phone = models.CharField(max_length = 32)
    salary = models.FloatField()

    def __str__(self):
        return 'Name: ' + str(self.name) + ' ' + 'Workshop: ' + str(self.workshop) \
            + ' ' + 'Phone: ' + str(self.phone) + ' ' + 'Salary: ' + str(self.salary)
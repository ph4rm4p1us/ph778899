from django.db import models
from Core.models import *
from Sales.models import *


# Create your models here.
class DeliveryEmployee(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee.user.first_name + '-' + self.employee.user.last_name + '-' + self.employee.phone


class ShippingArea(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    shipping_fees = models.FloatField()
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

    def __str__(self):
        return self.area.name + '-' + self.shipping_fees


class DeliveryInvoices(models.Model):
    invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE)
    shipped_to = models.ForeignKey(ClientAddress, on_delete=models.CASCADE)
    shipped_at = models.DateTimeField()
    shipped_with = models.ForeignKey(DeliveryEmployee, on_delete=models.CASCADE)
    shipping_info = models.ForeignKey(ShippingArea, on_delete=models.CASCADE)

    def __str__(self):
        return self.shipped_to.client.name

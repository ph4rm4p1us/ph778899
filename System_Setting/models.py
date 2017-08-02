from django.db import models
from Core.models import *


# Create your models here.


class SystemSettings(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    # Default Product Setting
    sell_online = models.BooleanField(default=True)
    sell_offline = models.BooleanField(default=True)
    trace_stock = models.BooleanField(default=False)
    min_stock = models.IntegerField(default=1)
    max_stock = models.IntegerField(default=1000)
    reminder_date = models.IntegerField(default=60)
    max_order = models.IntegerField(default=100)
    # Default Phone Setting
    show_main_phone = models.BooleanField(default=True)
    show_branch_phone = models.BooleanField(default=True)


class Product_Settings(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    product = models.ForeignKey(CoreMedicine, on_delete=models.CASCADE)
    # Default Product Setting
    sell_online = models.BooleanField(default=True)
    sell_offline = models.BooleanField(default=True)
    trace_stock = models.BooleanField(default=False)
    min_stock = models.IntegerField(default=1)
    max_stock = models.IntegerField(default=1000)
    reminder_date = models.IntegerField(default=60)
    max_order = models.IntegerField(default=100)

    def __str__(self):
        return self.pharmacy.name + str(self.product.id)

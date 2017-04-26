from django.db import models


# Create your models here.


class SalesInvoice(models.Model):
    date_time = models.DateTimeField(blank=False)
    total_price = models.FloatField(blank=False, default=0.0)
    status = models.BooleanField(blank=False, default=0)
    client_name = models.CharField(blank=False, max_length=60)
    sold_by = models.CharField(blank=False, max_length=60)
    branch_name = models.CharField(blank=False, max_length=200)
    pharmacy = models.ForeignKey('Core.Pharmacy', on_delete=models.CASCADE)
    # items_column


class InvoiceItems(models.Model):
    medicine = models.CharField(blank=False, max_length=200)
    sales_price = models.FloatField(blank=False, default=0.0)
    purchase_price = models.FloatField(blank=False, default=0.0)
    net_price = models.FloatField(blank=False, default=0.0)
    discount = models.IntegerField(blank=False, max_length=3)
    reverse = models.BooleanField(blank=False, default=0)




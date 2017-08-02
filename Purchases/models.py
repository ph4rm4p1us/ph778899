from django.db import models

# Create your models here.


class PurchasesInvoice(models.Model):
    medicine = models.CharField(max_length=200, blank=False)
    tax = models.FloatField(blank=False, default=0.0)
    expiration_date = models.DateTimeField(blank=False)
    supplier = models.CharField(max_length=200, blank=False)
    process_date = models.DateTimeField(blank=False, auto_now_add=True)
    branch_name = models.CharField(max_length=200, blank=False)
    pharmacy = models.ForeignKey('Core.Pharmacy', on_delete=models.CASCADE)


class PurchaseItems(models.Model):
    medicine_name = models.CharField(blank=False, max_length=200)
    sales_price = models.FloatField(blank=False, default=0.0)
    purchase_price = models.FloatField(blank=False, default=0.0)
    net_price = models.FloatField(blank=False, default=0.0)
    bounce = models.FloatField()
    discount = models.IntegerField(blank=False)
    purchase_invoice_id = models.ForeignKey(PurchasesInvoice, on_delete=models.CASCADE)





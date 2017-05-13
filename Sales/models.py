from django.db import models
from django.contrib.auth.models import Permission, User


# Create your models here.


class SalesInvoice(models.Model):
    date = models.DateTimeField(blank=False)
    total_price = models.FloatField(default=0.0)
    status = models.SmallIntegerField(default=0)
    # 0: Not Saved    1: Saved, Not Assigned   2: Saved, Paid
    client_name = models.ForeignKey('Core.Clients', on_delete=models.CASCADE, null=True)
    sold_by = models.ForeignKey('Core.Employees', on_delete=models.CASCADE)
    branch = models.ForeignKey('Core.Branches', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class InvoiceItems(models.Model):
    invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE)
    item = models.ForeignKey('Stock.MedicineStock', on_delete=models.CASCADE)
    main_unit_price = models.FloatField(default='Stock.MedicineStock.main_unit_price')
    med_unit_price = models.FloatField(default=0)
    main_unit_quantity = models.IntegerField(default=0)
    med_unit_quantity = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)
    discount = models.IntegerField(default=0)




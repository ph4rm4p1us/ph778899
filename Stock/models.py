from django.db import models
# Create your models here.


class MedicineStock(models.Model):
    main_unit_stock = models.IntegerField(blank=False)
    med_unit_stock = models.IntegerField(blank=False)
    main_unit_price = models.FloatField(blank=False)
    med_unit_price = models.FloatField(blank=False)
    expiration = models.DateTimeField(blank=False)
    purchase_price = models.FloatField(blank=False)
    purchase_discount = models.IntegerField(blank=False)
    bounce = models.IntegerField()
    # for counting the deficient
    min_amount = models.IntegerField(blank=False)
    pharmacy = models.ForeignKey('Core.Pharmacy', on_delete=models.CASCADE)


class MedicineSettings(models.Model):
    sell_online = models.BooleanField(blank=False, default=0)
    sell_offline = models.BooleanField(blank=False, default=0)
    trace_stock = models.BooleanField(blank=False, default=0)
    min_stock = models.IntegerField()
    max_stock = models.IntegerField()
    expiration_date = models.DateTimeField(blank=False)
    reminder_date = models.DateTimeField(blank=False)
    max_order = models.IntegerField()
    pharmacy = models.ForeignKey('Core.Pharmacy', on_delete=models.CASCADE)




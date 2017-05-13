from django.db import models
# Create your models here.


class MedicineStock(models.Model):
    item = models.ForeignKey('Core.CoreMedicine', on_delete=models.CASCADE)
    main_unit_stock = models.IntegerField(blank=False)
    med_unit_stock = models.IntegerField(blank=False)
    main_unit_price = models.FloatField(blank=False)
    med_unit_price = models.FloatField(blank=False)
    expiration = models.DateField(blank=False)
    purchase_price = models.FloatField(blank=False)
    purchase_discount = models.IntegerField(blank=False)
    bounce = models.IntegerField()
    branch = models.ForeignKey('Core.Branches', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item) + '-' + \
               str(self.main_unit_stock) + ':' + \
               str(self.med_unit_stock) + '-' + \
               str(self.expiration)

    def __get_settings__(self):
        return MedicineSettings.objects.get(item=self.item)


class MedicineSettings(models.Model):
    item = models.ForeignKey('Core.CoreMedicine', on_delete=models.CASCADE, null=True)
    sell_online = models.BooleanField(blank=False, default=0)
    sell_offline = models.BooleanField(blank=False, default=0)
    trace_stock = models.BooleanField(blank=False, default=0)
    min_stock = models.IntegerField()
    max_stock = models.IntegerField()
    reminder_date = models.IntegerField(blank=False)
    max_order = models.IntegerField()
    pharmacy = models.ForeignKey('Core.Pharmacy', on_delete=models.CASCADE)

    def __str__(self):
        return self.item




from django.db import models

# Create your models here.


class Safe(models.Model):
    operation_by = models.CharField(blank=False, max_length=45)
    bounce = models.FloatField(default=0.0, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=False)
    pharmacy = models.ForeignKey('Core.Pharmacy', on_delete=models.CASCADE)


class LastWithdraw(models.Model):
    process_date = models.DateTimeField(auto_now_add=True, blank=False)
    value = models.FloatField(default=0.0, blank=False)
    safe_id = models.ForeignKey(Safe, on_delete=models.CASCADE)

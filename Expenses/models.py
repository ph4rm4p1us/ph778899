from django.db import models

# Create your models here.


class Expenses(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=False)
    notes = models.CharField(blank=False, max_length=200)
    pharmacy = models.ForeignKey('Core.Pharmacy', on_delete=models.CASCADE)


class Destination(models.Model):
    name = models.CharField(blank=False, max_length=100)
    expenses_id = models.ForeignKey(Expenses, on_delete=models.CASCADE)
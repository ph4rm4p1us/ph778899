from Core.models import *
from django.db import models


# Create your models here.
class Treasury(models.Model):
    name = models.CharField(max_length=128)
    type = models.SmallIntegerField(default=1)       #0:Main  , 1:Secondary,  2:bank
    current_balance = models.FloatField(default=0)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TreasuryAuth(models.Model):
    treasury = models.ForeignKey(Treasury, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + '-' + self.user.last_name + '-' + self.treasury.name


class TreasuryTransaction(models.Model):
    treasury = models.ForeignKey(Treasury, on_delete=models.CASCADE)
    amount = models.FloatField()
    done_by = models.CharField(max_length=128)
    comment = models.CharField(max_length=512)

    def __str__(self):
        return self.treasury.name + '-' + self.amount + '-' + self.comment


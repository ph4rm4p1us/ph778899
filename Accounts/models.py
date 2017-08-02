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


class CustomerAccounts(models.Model):
    customer = models.ForeignKey(Clients, on_delete=models.CASCADE)
    credit = models.FloatField(default=0)
    debit = models.FloatField(default=0)
    comment = models.CharField(max_length=256)
    date = models.DateTimeField()

    def __str__(self):
        return self.customer.name + '-' + self.comment


class BankAccounts(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    bank = models.CharField(max_length=64)
    account_number = models.IntegerField()
    balance = models.FloatField()
    currency = models.CharField(max_length=64)

    def __str__(self):
        return self.bank + str(self.account_number)

    def __balance__(self):
        return str(self.balance) + self.currency


class ExpenseCategory(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    parent = models.IntegerField(default=0)

    def get_parent(self):
        if self.parent == 0:
            return False
        else:
            parent_category = ExpenseCategory.objects.get(id=self.parent)
            return parent_category

    def __str__(self):
        parent = ExpenseCategory.get_parent(self)
        if not parent:
            return self.name
        else:
            return str(parent) + " > " + self.name


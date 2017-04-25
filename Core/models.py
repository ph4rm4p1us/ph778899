from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.
class Pharmacy(models.Model):
    owner = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Pharmacy_Employee(models.Model):
    user = models.ForeignKey(User, unique=True)
    pharmacy = models.ForeignKey(Pharmacy)
    phone = models.CharField(max_length=15)
    national_id = models.IntegerField(max_length=14)

class Medicine_DB(models.Model):
    int_barcode = models.IntegerField()





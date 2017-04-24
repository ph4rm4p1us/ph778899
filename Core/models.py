from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.
'''
class Pharmacy(models.Model):
    owner = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

'''


class CoreMedicine(models.Model):
    barcode = models.CharField(max_length=32)
    comerical_name = models.CharField(max_length=200)
    arabic_name = models.CharField(max_length=200)






#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import Permission, User


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class TaxGroup(models.Model):
    name = models.CharField(max_length=64)
    tax_type = models.SmallIntegerField()
    tax_percent = models.IntegerField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)
    tax_group = models.ForeignKey(TaxGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MedicineType(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return self.type


class GenericName(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Licence(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class CoreMedicine(models.Model):
    barcode = models.CharField(blank=False, max_length=32)
    commercial_name = models.CharField(blank=False, max_length=200)
    arabic_name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(MedicineType, on_delete=models.CASCADE)
    generic_name = models.ForeignKey(GenericName, on_delete=models.CASCADE)
    price = models.FloatField(blank=False, default=0.0)
    med_unit_price = models.FloatField(blank=False, default=0.0)
    small_unit_price = models.FloatField(blank=True, null=True, default=0.0)
    med_unit = models.IntegerField(blank=False, max_length=11)
    small_unit = models.IntegerField(blank=True, null=True, max_length=11)
    licence = models.ForeignKey(Licence, on_delete=models.CASCADE)
    storage_temp = models.IntegerField(max_length=3)

    def __str__(self):
        return self.commercial_name + '-' + self.barcode + '-' + self.arabic_name + '-' + self.brand.name + '-' + self.type.type


class Governorate(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=64)
    governorate = models.ForeignKey(Governorate, on_delete=models.CASCADE)

    def __str__(self):
        return self.governorate.name + '-' + self.name


class Area(models.Model):
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '-' + self.city.name + '-' + self.city.governorate.name


class Pharmacy(models.Model):
    name = models.CharField(max_length=100, blank=False)
    auth_user_email = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Branches(models.Model):
    name = models.CharField(max_length=200, blank=False)
    governorate = models.ForeignKey(Governorate, blank=False, null=True)
    city = models.ForeignKey(City, blank=False, null=True)
    area = models.ForeignKey(Area, blank=False, null=True)
    location = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

    def __str__(self):
        return self.pharmacy.name + '-' + self.name + '-' + self.phone + '-' + self.location


class Clients(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=15)
    allow_negative_balance = models.BooleanField(default=True)
    max_negative_balance = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    discount_percent = models.IntegerField(max_length=3, blank=False, default=0)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name + '-' + self.phone


class ClientAddress(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    second_phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.client.name + '-' + self.area.name + '-' + self.address


class Employees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=15, blank=False)
    address = models.CharField(max_length=200, blank=False)
    national_id = models.IntegerField(null=True)
    balance = models.FloatField(default=0)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


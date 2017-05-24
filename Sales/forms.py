#-*- coding: utf-8 -*-
from django import forms
from .models import *
from Stock.models import *
from Accounts.models import *


class AddItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItems
        fields = [
            'main_unit_quantity',
            'med_unit_quantity',
            'main_unit_price',
            'med_unit_price',
            'discount',
        ]
        labels = {
            'main_unit_quantity': 'الكمية',
            'med_unit_quantity': "كمية الوحدات الوسطي",
            'main_unit_price': "سعر الوحدة",
            'med_unit_price': "سعر الوحدة الوسطي",
            'discount': "الخصم",
        }
        widgets = {
            'main_unit_quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الكمية'}),
            'med_unit_quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'الوحدات المتوسطة'}),
            'main_unit_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سعر الوحدة'}),
            'med_unit_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سعر الوحدة المتوسطة'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'خصم'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'إجمالي السعر'}),
        }


class PayForm(forms.ModelForm):
    class Meta:
        model = CustomerAccounts
        fields = [
            'customer',
            'debit',
        ]

        labels = {
            'customer': 'العميل',
            'debit': "المدفوع",
        }
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control select2'}),
            'debit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'المدفوع', 'onkeyup': 'get_change();'}),
        }


class CustomerReports(forms.ModelForm):
    class Meta:
        model = SalesInvoice
        fields = [
            'customer',
        ]

        labels = {
            'customer': 'العميل',
        }
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control select2'}),
        }


class ProductReports(forms.ModelForm):
    class Meta:
        model = MedicineStock
        fields = [
            'item',
        ]

        labels = {
            'item': 'الصنف',
        }
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control select2'}),
        }


class ReverseInvoiceForm(forms.ModelForm):
    class Meta:
        model = SalesInvoice
        fields = [
            'id'
        ]
        labels = {
            'id': "رقم الفاتورة"
        }
        widgets = {
            'id': forms.Select(attrs={'class': 'form-control'})
        }

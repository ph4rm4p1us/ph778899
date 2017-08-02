#-*- coding: utf-8 -*-
from django import forms
from .models import *
from Stock.models import *
from Accounts.models import *


class ProductSettingsForm(forms.ModelForm):
    class Meta:
        model = Product_Settings
        fields = [
            'sell_online',
            'sell_offline',
            'trace_stock',
            'min_stock',
            'max_stock',
            'reminder_date',
            'max_order',
        ]
        labels = {
            'sell_online': 'السماح بالبيع اون لاين',
            'sell_offline': "السماح للمنتجات بالبيع في الفروع",
            'trace_stock': "تتبع المخزون للمنتجات",
            'min_stock': "الكمية الحرجة من المنتجات",
            'max_stock': "الكمية القصوي من المنتجات",
            'reminder_date': "التحذير قبل الصلاحية ب",
            'max_order': "اقصي كمية يمكن بيعها في نفس الاوردر",
        }
        widgets = {
            'min_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'reminder_date': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class SystemSettingsForm(forms.ModelForm):
    class Meta:
        model = SystemSettings
        fields = [
            'sell_online',
            'sell_offline',
            'trace_stock',
            'min_stock',
            'max_stock',
            'reminder_date',
            'max_order',
            'show_main_phone',
            'show_branch_phone',
        ]
        labels = {
            'sell_online': 'السماح بالبيع اون لاين',
            'sell_offline': "السماح للمنتجات بالبيع في الفروع",
            'trace_stock': "تتبع المخزون للمنتجات",
            'min_stock': "الكمية الحرجة من المنتجات",
            'max_stock': "الكمية القصوي من المنتجات",
            'reminder_date': "التحذير قبل الصلاحية ب",
            'max_order': "اقصي كمية يمكن بيعها في نفس الاوردر",
            'show_main_phone': "إظهار رقم التليفون الرئيسي للصيدلية",
            'show_branch_phone': "اظهار رقم الفرع",
        }
        widgets = {
            'min_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'reminder_date': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_order': forms.NumberInput(attrs={'class': 'form-control'}),
        }
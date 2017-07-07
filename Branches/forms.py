#-*- coding: utf-8 -*-
from django import forms
from Core.models import *


class AddBranch(forms.ModelForm):
    class Meta:
        model = Branches
        fields = [
            'name',
            'governorate',
            'city',
            'area',
            'location',
            'phone',
            'manager',
        ]
        labels = {
            'name': 'اسم الفرع',
            'governorate': 'المحافظة',
            'city': 'المدينة',
            'area': 'المنطقة',
            'location': "عنوان الفرع",
            'phone': "رقم التليفون",
            'manager': "مدير الفرع",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم الفرع'}),
            'governorate': forms.Select(attrs={'class': 'select2 form-control', 'placeholder': 'المحافظة'}),
            'city': forms.Select(attrs={'class': 'select2 form-control', 'placeholder': 'المدينة'}),
            'area': forms.Select(attrs={'class': 'select2 form-control', 'placeholder': 'المنطقة'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان الفرع'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'رقم التليفون'}),
            'manager': forms.Select(attrs={'class': 'select2 form-control', 'placeholder': 'مدير الفرع'}),
        }
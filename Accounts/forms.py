#-*- coding: utf-8 -*-
from django import forms
from .models import *


class AddTreasury(forms.ModelForm):

    class Meta:
        model = Treasury
        fields = [
            'name',
            ]

        labels = {
            'name': "اسم الخزينة",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم الخزينة'}),
        }


class AddBankAccount(forms.ModelForm):

    class Meta:
        model = Treasury
        fields = [
            'name',
            'account_number',
            'currency',
            ]

        labels = {
            'name': "اسم البنك",
            'account_number': "رقم الحساب",
            'currency': "العملة",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم البنك'}),
            'account_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'رقم الحساب'}),
            'currency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'العملة'}),
        }

class AddExpenseCategory(forms.ModelForm):

    class Meta:
        model = ExpenseCategory
        fields = [
            'name',
            ]

        labels = {
            'name': "اسم التصنيف",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم التصنيف'}),
        }
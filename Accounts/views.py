from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from Core.views import *


# Create your views here.
@login_required(login_url='Core:login_user')
def index(request):
    context = {}
    return render(request, 'Accounts/accountsHome.html', context)


@login_required(login_url='Core:login_user')
def bank_accounts(request):
    page_title = 'إدارة الحسابات البنكية'
    accounts = BankAccounts.objects.filter(pharmacy=get_pharmacy(request))
    context = {
        'page_title': page_title,
        'accounts': accounts,
    }
    return render(request, 'Accounts/bankAccounts.html', context)


@login_required(login_url='Core:login_user')
def add_bank_account(request):
    page_title = 'إضافة حساب بنكي'
    form = AddBankAccount(request.POST or None)
    message = ""
    if form.is_valid():
        account = form.save(commit=False)
        account.pharmacy = get_pharmacy(request)
        account.balance = 0
        account.save()
        message = "تم إضافة الحساب بنجاح"
    context = {
        'page_title': page_title,
        'form': form,
        'message': message,
    }
    return render(request, 'Accounts/addBankAccount.html', context)


@login_required(login_url='Core:login_user')
def edit_bank_account(request, account_id):
    page_title = 'تعديل حساب بنكي'
    this_account = BankAccounts.objects.get(id=account_id)
    if this_account.pharmacy != get_pharmacy(request):
        return permission_error(request)
    form = AddBankAccount(request.POST or None, instance=this_account)
    message = ""
    if form.is_valid():
        account = form.save(commit=False)
        account.save()
        message = "تم تعديل الحساب بنجاح"
    context = {
        'page_title': page_title,
        'form': form,
        'message': message,
    }
    return render(request, 'Accounts/addBankAccount.html', context)


@login_required(login_url='Core:login_user')
def delete_bank_account(request, account_id):
    this_account = get_object_or_404(BankAccounts, id=account_id)
    if this_account.pharmacy != get_pharmacy(request):
        return permission_error(request)
    this_account.delete()
    return bank_accounts(request)


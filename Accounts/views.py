from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import *
from .forms import *
from Core.views import *


# Create your views here.
@login_required(login_url='Core:login_user')
def index(request):
    context = {}
    return render(request, 'Accounts/accountsHome.html', context)


@login_required(login_url='Core:login_user')
def treasury(request):
    page_title = 'إدارة الخزائن'
    content = Treasury.objects.filter(pharmacy=get_pharmacy(request), type__in=[0, 1])
    context = {
        'page_title': page_title,
        'content': content,
    }
    return render(request, 'Accounts/treasury.html', context)


@login_required(login_url='Core:login_user')
def add_treasury(request):
    page_title = 'إضافة خزينة'
    message = ''
    form = AddTreasury(request.POST or None)
    if form.is_valid():
        treasury = form.save(commit=False)
        treasury.type = request.POST['type']
        treasury.pharmacy = get_pharmacy(request)
        treasury.save()
        message = 'تم إضافة الخزينة بنجاح'
    context = {
        'page_title': page_title,
        'form': form,
        'message': message,
    }
    return render(request, 'Accounts/addTreasury.html', context)


@login_required(login_url='Core:login_user')
def edit_treasury(request, pk):
    page_title = 'تعديل خزينة'
    this = get_object_or_404(Treasury, id=pk)
    message = ''
    form = AddTreasury(request.POST or None, instance=this)
    if form.is_valid():
        treasury = form.save(commit=False)
        treasury.type = request.POST['type']
        treasury.pharmacy = get_pharmacy(request)
        treasury.save()
        message = 'تم تعديل الخزينة بنجاح'
    context = {
        'page_title': page_title,
        'form': form,
        'message': message,
        'this': this,
    }
    return render(request, 'Accounts/addTreasury.html', context)


@login_required(login_url='Core:login_user')
def delete_treasury(request, pk):
    this = get_object_or_404(Treasury, id=pk)
    if this.pharmacy != get_pharmacy(request):
        return permission_error(request)
    else:
        this.delete()
        return treasury(request)


@login_required(login_url='Core:login_user')
def bank_accounts(request):
    page_title = 'إدارة الحسابات البنكية'
    accounts = Treasury.objects.filter(pharmacy=get_pharmacy(request), type=3)
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
        account.type = 3
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
    this_account = Treasury.objects.get(id=account_id)
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
    this_account = get_object_or_404(Treasury, id=account_id)
    if this_account.pharmacy != get_pharmacy(request):
        return permission_error(request)
    this_account.delete()
    return bank_accounts(request)


@login_required(login_url='Core:login_user')
def expense_category(request):
    page_title = 'إدارة تصنيفات المصاريف'
    categories = ExpenseCategory.objects.filter(pharmacy=get_pharmacy(request))
    context = {
        'page_title': page_title,
        'categories': categories,
    }
    return render(request, 'Accounts/expenseCategory.html', context)


@login_required(login_url='Core:login_user')
def expense_category(request):
    page_title = 'تصنيفات المصاريف'
    categories = ExpenseCategory.objects.filter(pharmacy=get_pharmacy(request))
    context = {
        'page_title': page_title,
        'categories': categories,
    }
    return render(request, 'Accounts/expenseCategory.html', context)


@login_required(login_url='Core:login_user')
def add_expense_category(request):
    form = AddExpenseCategory(request.POST or None)
    message = ''
    page_title = 'إضافة تصنيف للمصاريف'
    form = AddExpenseCategory(request.POST or None)
    categories = ExpenseCategory.objects.filter(pharmacy=get_pharmacy(request))
    if form.is_valid():
        category = form.save(commit=False)
        category.pharmacy = get_pharmacy(request)
        category.parent = request.POST.get('parent', 0)
        category.save()
        message = 'تم إضافة التصنيف بنجاح'
    context = {
        'page_title': page_title,
        'categories': categories,
        'form': form,
        'message': message,
    }
    return render(request, 'Accounts/addExpneseCategory.html', context)


@login_required(login_url='Core:login_user')
def edit_expense_category(request, account_id):
    this = get_object_or_404(ExpenseCategory, id=account_id)
    parent = this.get_parent()
    form = AddExpenseCategory(request.POST or None, instance=this)
    message = ''
    page_title = 'إضافة تصنيف للمصاريف'
    categories = ExpenseCategory.objects.filter(pharmacy=get_pharmacy(request))
    if form.is_valid():
        category = form.save(commit=False)
        category.pharmacy = get_pharmacy(request)
        category.parent = request.POST['parent']
        category.save()
        message = 'تم إضافة التصنيف بنجاح'
    context = {
        'page_title': page_title,
        'categories': categories,
        'form': form,
        'message': message,
        'parent': parent,
        'this': this,
    }
    return render(request, 'Accounts/addExpneseCategory.html', context)


@login_required(login_url='Core:login_user')
def delete_expense_category(request, account_id):
    this = get_object_or_404(ExpenseCategory, id=account_id)
    if this.pharmacy != get_pharmacy(request):
        return permission_error(request)
    this.delete()
    return expense_category(request)


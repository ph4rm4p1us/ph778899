#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='Core:login_user')
def get_branch(request):
    employee = Employees.objects.get(user=request.user)
    branch = employee.branch
    return branch


@login_required(login_url='Core:login_user')
def get_employee(request):
    employee = Employees.objects.get(user=request.user)
    return employee


@login_required(login_url='Core:login_user')
def get_pharmacy(request):
    branch = get_branch(request)
    pharmacy = branch.pharmacy
    return pharmacy


@login_required(login_url='Core:login_user')
def index(request):
        context = {}
        return render(request, "Core/homepage.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(request.POST['next'], '/')
            else:
                return render(request, 'Core/login.html', {'error_message': 'تم إيقاف الحساب الخاص بك'})
        else:
            return render(request, 'Core/login.html', {'error_message': 'برجاء التأكد من اسم المستخدم وكلمة السر'})
    return render(request, 'Core/login.html')


@login_required(login_url='Core:login_user')
def logout_user(request):
    logout(request)
    return render(request, 'Core/login.html')


@login_required(login_url='Core:login_user')
def permission_error(request):
    page_title = 'خطأ في الصلاحيات'
    message = "غير مسموح لك بالتواجد داخل هذه الصفحة يمكنك الرجوع للصفحة السابقة من هنا"
    context = {
        'page_title': page_title,
        'message': message,
        }
    return render(request, 'Core/permission_error.html', context)




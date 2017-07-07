#-*- coding: utf-8 -*-
from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


# Create your views here.
def get_branch(request):
    employee = Employees.objects.get(user=request.user)
    branch = employee.branch
    return branch


def get_employee(request):
    employee = Employees.objects.get(user=request.user)
    return employee


def get_pharmacy(request):
    branch = get_branch(request)
    pharmacy = branch.pharmacy
    return pharmacy


def index(request):
    if not request.user.is_authenticated():
        return render(request, "Core/login.html")
    else:
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
                return render(request, 'Core/homepage.html')
            else:
                return render(request, 'Core/login.html', {'error_message': 'تم إيقاف الحساب الخاص بك'})
        else:
            return render(request, 'Core/login.html', {'error_message': 'برجاء التأكد من اسم المستخدم وكلمة السر'})
    return render(request, 'Core/login.html')


def logout_user(request):
    logout(request)
    return render(request, 'Core/login.html')
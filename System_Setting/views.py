from django.shortcuts import render
from Core.models import *
from Stock.models import *
from Core.views import *
from .models import *
from .forms import *


# Create your views here.
def index(request):
    context = {}
    return render(request, 'System_Setting/systemHome.html', context)


def set_default_settings(request, id):
    default_settings = SystemSettings.objects.get(pharmacy=get_pharmacy(request))
    setting = Product_Settings()
    setting.product_id = id
    setting.pharmacy = get_pharmacy(request)
    setting.sell_offline = default_settings.sell_offline
    setting.sell_online = default_settings.sell_online
    setting.min_stock = default_settings.min_stock
    setting.max_stock = default_settings.max_stock
    setting.max_order = default_settings.max_order
    setting.reminder_date = default_settings.reminder_date
    setting.trace_stock = default_settings.trace_stock
    setting.save()
    return setting


def product_setting(request):
    all_products = CoreMedicine.objects.all()
    if request.GET:
        id = request.GET['id']
        try:
            settings = Product_Settings.objects.get(product__id=id)
        except:
            settings = set_default_settings(request, id)
        form = ProductSettingsForm(request.POST or None, instance=settings)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'product': settings,
        }
        return render(request, 'System_Setting/get_product_settings.html', context)
    context = {
        'all_products': all_products,
    }
    return render(request, 'System_Setting/productSetting.html', context)


def default_system_setting(request):
    try:
        entry = SystemSettings.objects.get(pharmacy=get_pharmacy(request))
    except:
        entry = SystemSettings()
        entry.save()
    form = SystemSettingsForm(request.POST or None, instance=entry)
    if form.is_valid():
        default_settings = form.save(commit=False)
        default_settings.pharmacy = get_pharmacy(request)
        default_settings.save()
    context = {
        'form': form,
    }
    return render(request, 'System_Setting/defaultSetting.html', context)


def employee_management(request):
    users = Employees.objects.filter()
    context = {
        'users': users
    }
    return render(request, 'System_Setting/employee.html', context)








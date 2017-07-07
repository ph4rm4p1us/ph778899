from django.shortcuts import render
from Core.models import *
from Stock.models import *
from Core.views import *


# Create your views here.
def index(request):
    context = {}
    return render(request, 'System_Setting/systemHome.html', context)


def product_setting(request):
    all_products = CoreMedicine.objects.all()
    if request.GET:
        product_id = request.GET['id']
        try:
            setting =  MedicineSettings.objects.get(item__id=product_id)
        except:
            setting = default_settings(request, product_id)
    context = {}
    return render(request, 'System_Setting/productSetting.html', context)


def default_settings(request, product_id):
    setting = MedicineSettings()
    setting.item_id = product_id
    setting.pharmacy = get_pharmacy(request)


    pass
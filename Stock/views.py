from django.shortcuts import render
from .models import *
from Core.views import *


# Create your views here.
def index(request):
    context = {}
    return render(request, 'Stock/stockHome.html', context)


def get_stock(request, product_id):
    stock = MedicineStock.objects.filter(item_id=product_id, branch=get_branch(request), main_unit_stock__gt=0)
    context = {
        'stock': stock,
    }
    return render(request, 'Stock/get_stock_options.html', context)




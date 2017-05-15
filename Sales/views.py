from django.shortcuts import render, redirect
from .models import *
from .forms import *
from Core.models import *
from Core.views import *
from Stock.models import *
from datetime import datetime


# Create your views here.
def get_perv_invoice(request, inv_id):
    this_invoice = SalesInvoice.objects.get(id=inv_id)
    perv_invoices = SalesInvoice.objects.filter(branch=get_branch(request)).filter(id__lt=this_invoice.id).order_by('-id')[0:1]
    if perv_invoices.count() >=1:
        for x in perv_invoices:
            perv_invoice = x
    else:
        perv_invoice = this_invoice
    return perv_invoice


def get_next_invoice(request, inv_id):
    this_invoice = SalesInvoice.objects.get(id=inv_id)
    next_invoices = SalesInvoice.objects.filter(branch=get_branch(request)).filter(id__gt=this_invoice.id).order_by('id')[0:1]
    if next_invoices.count() >= 1:
        for x in next_invoices:
            next_invoice = x
    else:
        next_invoice = this_invoice
    return next_invoice


def index(request):
    context = {}
    return render(request, 'Sales/salesHome.html', context)


def reduce_stock(request, item_id, main_unit_qnt, med_unit_qnt):
    try:
        current_stock = MedicineStock.objects.get(id=item_id)
        current_main_stock = current_stock.main_unit_stock
        current_med_stock = current_stock.med_unit_stock
        new_main_stock = current_main_stock - main_unit_qnt
        new_med_stock = current_med_stock - med_unit_qnt
        current_stock.main_unit_stock = new_main_stock
        current_stock.med_unit_stock = new_med_stock
        current_stock.save()
        return True
    except:
        return False


def add_item_to_sales_invoice(request, invoice_id):
    this_invoice = SalesInvoice.objects.get(id=invoice_id)
    if request.GET:
        item_id = request.GET['item']
    this_stock = MedicineStock.objects.get(id=item_id)
    form = AddItemForm(request.POST or None, initial={
        'main_unit_price': this_stock.main_unit_price,
        'med_unit_price': this_stock.med_unit_price,
    })

    error_message = ''
    if form.is_valid():
        invoice_item = form.save(commit=False)
        invoice_item.invoice = SalesInvoice.objects.get(id=invoice_id)
        invoice_item.item = MedicineStock.objects.get(id=item_id)
        invoice_item.total_price = (form.cleaned_data['main_unit_quantity'] * form.cleaned_data['main_unit_price']) + \
                                   (form.cleaned_data['med_unit_quantity'] * form.cleaned_data['med_unit_price']) - \
                                   form.cleaned_data['discount']
        if reduce_stock(request, item_id, form.cleaned_data['main_unit_quantity'], form.cleaned_data['med_unit_quantity']):
            invoice_item.save()
            error_message = 'تم'
        else:
            error_message = "خطأ"

    context = {
        'form': form,
        'this_stock': this_stock,
        'error_message': error_message,
    }
    return render(request, 'Sales/invoice_items.html', context)


def edit_invoice(request, invoice_id):
    if request.GET:
        item_id = request.GET['item']
        this_stock = MedicineStock.objects.filter(item_id=item_id, branch=get_branch(request)).order_by('expiration')
        '''form = AddItemForm(request.POST or None, initial={
            'main_unit_price': this_stock[0].main_unit_price,
            'med_unit_price': this_stock[0].med_unit_price,
        })
        if form.is_valid():
            invoice_item = form.save(commit=False)
            invoice_item.invoice = SalesInvoice.objects.get(id=invoice_id)
            invoice_item.item = MedicineStock.objects.get(id=item_id)
            invoice_item.total_price = (form.cleaned_data['main_unit_quantity'] * form.cleaned_data['main_unit_price']) + \
                                       (form.cleaned_data['med_unit_quantity'] * form.cleaned_data['med_unit_price']) - \
                                       form.cleaned_data['discount']
            if reduce_stock(request, item_id, form.cleaned_data['main_unit_quantity'], form.cleaned_data['med_unit_quantity']):
                invoice_item.save()
                error_message = 'تم'
            else:
                error_message = "خطأ"'''
    this_invoice = SalesInvoice.objects.get(id=invoice_id)
    this_invoice_items = InvoiceItems.objects.filter(invoice=this_invoice.id)
    this_invoice_total = 0
    for x in this_invoice_items:
        this_invoice_total += x.total_price
    all_items = CoreMedicine.objects.all()
    perv_invoice = get_perv_invoice(request, invoice_id)
    next_invoice = get_next_invoice(request, invoice_id)
    context = {
        'this_invoice': this_invoice,
        'this_invoice_items': this_invoice_items,
        'all_items': all_items,
        'perv_invoice': perv_invoice,
        'next_invoice': next_invoice,
        'this_invoice_total': this_invoice_total,
    }
    '''if request.GET:
        context.update({
            'form': form,
            'this_stock': this_stock
        })'''
    return render(request, 'Sales/invoice_maker.html', context)


def new_invoice(request):
    invoice = SalesInvoice()
    invoice.date = datetime.now()
    invoice.total_price = 0.0
    invoice.status = 0
    invoice.sold_by = get_employee(request)
    invoice.branch = get_branch(request)
    invoice.save()
    invoice_id = invoice.id
    this_invoice = SalesInvoice.objects.get(id=invoice_id)
    context = {
        'this_invoice': this_invoice,
    }
    return redirect('../'+str(invoice_id)+'/')



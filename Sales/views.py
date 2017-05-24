from django.shortcuts import render, redirect
from .models import *
from .forms import *
from Core.models import *
from Core.views import *
from Stock.models import *
from datetime import datetime, timedelta
from django.db.models import Sum, Avg, Count


# Create your views here.
def get_perv_invoice(request, inv_id):
    this_invoice = SalesInvoice.objects.get(id=inv_id)
    perv_invoices = SalesInvoice.objects.filter(branch=get_branch(request)).filter(id__lt=this_invoice.id).order_by(
        '-id')[0:1]
    if perv_invoices.count() >= 1:
        for x in perv_invoices:
            perv_invoice = x
    else:
        perv_invoice = this_invoice
    return perv_invoice


def get_next_invoice(request, inv_id):
    this_invoice = SalesInvoice.objects.get(id=inv_id)
    next_invoices = SalesInvoice.objects.filter(branch=get_branch(request)).filter(id__gt=this_invoice.id).order_by(
        'id')[0:1]
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
        invoice_item.invoice = this_invoice
        invoice_item.item = MedicineStock.objects.get(id=item_id)
        invoice_item.total_price = (form.cleaned_data['main_unit_quantity'] * form.cleaned_data['main_unit_price']) + \
                                   (form.cleaned_data['med_unit_quantity'] * form.cleaned_data['med_unit_price']) - \
                                   form.cleaned_data['discount']
        get_invoice_total(request, invoice_id)
        if reduce_stock(request, item_id, form.cleaned_data['main_unit_quantity'],
                        form.cleaned_data['med_unit_quantity']):
            invoice_item.save()
            error_message = 'تم'
        else:
            error_message = "خطأ"

    context = {
        'form': form,
        'this_stock': this_stock,
        'error_message': error_message,
    }
    return render(request, 'Sales/add_items.html', context)


def edit_invoice(request, invoice_id):
    if request.GET:
        item_id = request.GET['item']
        this_stock = MedicineStock.objects.filter(item_id=item_id, branch=get_branch(request)).order_by('expiration')

    this_invoice = SalesInvoice.objects.get(id=invoice_id)
    not_saved = False
    if this_invoice.status == 0:
        not_saved = True
    can_pay = False
    if this_invoice.status == 1:
        can_pay = True

    this_invoice_items = InvoiceItems.objects.filter(invoice=this_invoice.id)
    this_invoice_total = 0
    for x in this_invoice_items:
        this_invoice_total += x.total_price
    all_items = CoreMedicine.objects.all()
    perv_invoice = get_perv_invoice(request, invoice_id)
    next_invoice = get_next_invoice(request, invoice_id)
    context = {
        'not_saved': not_saved,
        'this_invoice': this_invoice,
        'this_invoice_items': this_invoice_items,
        'all_items': all_items,
        'perv_invoice': perv_invoice,
        'next_invoice': next_invoice,
        'this_invoice_total': this_invoice_total,
        'can_pay': can_pay,
    }
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
    return redirect('../' + str(invoice_id) + '/')


def save_invoice(request, invoice_id):
    try:
        this_invoice = SalesInvoice.objects.get(id=invoice_id)
        this_invoice.status = 1
        this_invoice.save()
        get_invoice_total(request, invoice_id)
        message = 'تم حفظ الفاتورة'
        message_type = 'success'
    except:
        message = 'هذا المحتوي غير موجود'
        message_type = 'danger'
    context = {
        'message': message,
        'message_type': message_type,
    }
    return render(request, 'Core/response.html', context)


def pay_invoice(request, invoice_id):
    try:
        this_invoice = SalesInvoice.objects.get(id=invoice_id)
        this_invoice.status = 2
        this_invoice.save()
        message = 'تم دفع الفاتورة'
        message_type = 'succes'
    except:
        message = 'هذا المحتوي غير موجود'
        message_type = 'danger'
    context = {
        'message': message,
        'message_type': message_type,
    }
    return render(request, 'Core/response.html', context)


def invoice_payment(request, invoice_id):
    this_invoice = SalesInvoice.objects.get(id=invoice_id)
    form = PayForm(request.POST or None)
    if form.is_valid():
        payment = form.save(commit=False)
        payment.date = datetime.now()
        payment.credit = this_invoice.total_price
        payment.comment = "فاتورة رقم "
        payment.comment += str(this_invoice.id)
        payment.save()
        this_invoice.customer = payment.customer
        this_invoice.save()
        pay_invoice(request, invoice_id)
    context = {
        'form': form,
        "this_invoice": this_invoice
    }
    return render(request, 'Sales/payment.html', context)


def get_invoice_total(request, invoice_id):
    this_invoice = SalesInvoice.objects.get(id=invoice_id)
    invoice_items = InvoiceItems.objects.filter(invoice=this_invoice)
    total = 0
    for item in invoice_items:
        total += item.total_price
    this_invoice.total_price = total
    this_invoice.save()


def cancel_invoice(request, invoice_id):
    this_invoice = SalesInvoice.objects.get(id=invoice_id)
    invoice_items = InvoiceItems.objects.filter(invoice=this_invoice)
    for x in invoice_items:
        reduce_stock(request, x.item.id, -x.main_unit_quantity, -x.med_unit_quantity)
    this_invoice.delete()
    perv_invoice = get_perv_invoice(request, invoice_id)
    return redirect('../../' + str(perv_invoice.id) + '/')


def sales_reports(request):
    return render(request, 'Sales/salesReports.html')


def customer_reports(request):
    form = CustomerReports(request.GET or None)
    context = {
        'form': form,
    }
    if request.GET:
        if form.is_valid():
            customer_id = request.GET['customer']
            from_date = request.GET['from']
            to_date = datetime.combine(datetime.strptime(request.GET['to'], '%Y-%m-%d').date(), datetime.max.time())
            this_customer = Clients.objects.get(id=customer_id)
            invoices = SalesInvoice.objects.filter(customer=this_customer, date__range=[from_date, to_date])
            customer_payments = CustomerAccounts.objects.filter(customer=this_customer, date__range=[from_date, to_date])
            items = []
            first_date = '1970-01-01'
            old_payments = CustomerAccounts.objects.filter(customer=this_customer, date__range=[first_date, from_date])
            debit = 0
            credit = 0
            total_debits = 0
            total_credits = 0
            items_total_price = 0
            old_payments_debit = CustomerAccounts.objects.values('customer__name', 'date').annotate(Sum('debit'))

            for payment in customer_payments:
                total_debits += payment.debit
                total_credits += payment.credit

            for payment in old_payments:
                debit += payment.debit
                credit += payment.credit
                total_debits += payment.debit
                total_credits += payment.credit

            for an_invoice in invoices:
                invoice_items = InvoiceItems.objects.filter(invoice=an_invoice)
                for item in invoice_items:
                    items.append(item)
                    items_total_price += item.total_price

            context = {
                'this_customer': this_customer,
                'invoices': invoices,
                'items': items,
                'customer_payments': customer_payments,
                'debit': debit,
                'credit': credit,
                'total_debits': total_debits,
                'total_credits': total_credits,
                'items_total_price': items_total_price,
                'old_payments_debit': old_payments_debit,
            }
    return render(request, 'Sales/customerReports.html', context)


def product_reports(request):
    form = ProductReports(request.GET or None)
    context = {
        'form': form,
    }
    if request.GET:
        product_id = request.GET['item']
        from_date = request.GET['from']
        to_date = datetime.combine(datetime.strptime(request.GET['to'], '%Y-%m-%d').date(), datetime.max.time())
        this_item = CoreMedicine.objects.get(id=product_id)
        item_statics = InvoiceItems.objects.values('item__item_id') \
            .annotate(main_unit_quantity=Sum('main_unit_quantity'), med_unit_quantity=Sum('med_unit_quantity'), total_price=Sum('total_price') ) \
            .filter(main_unit_quantity__gt=0, item__item_id=product_id, invoice__date__range=[from_date, to_date]) \
            .order_by('-main_unit_quantity')

        context = {
            'this_item': this_item,
            'item_statics': item_statics,
        }
    return render(request, 'Sales/productReports.html', context)


def invoice_reports(request):
    form = True
    context = {
        'form': form
    }
    if request.GET:
        from_date = request.GET['from']
        to_date = datetime.combine(datetime.strptime(request.GET['to'], '%Y-%m-%d').date(), datetime.max.time())
        invoices = SalesInvoice.objects.values('status') \
            .annotate(invoices_count=Count('id'), total_price=Sum('total_price')) \
            .filter(branch=get_branch(request), date__range=[from_date, to_date]) \
            .order_by('-status')
        context = {
            'invoices': invoices,

        }
    return render(request, 'Sales/invoiceReports.html', context)


def reverse(request):
    form = ReverseInvoiceForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        invoice_id = request.POST['id']
        invoice_items = InvoiceItems.objects.filter(invoice__id=invoice_id)
        context.update({'invoice_items': invoice_items})
    return render(request, 'Sales/reverse.html', context)


def get_invoice_items(request, invoice_id):
    invoice_items = InvoiceItems.objects.filter(invoice__id=invoice_id)
    this_invoice = SalesInvoice.objects.get(id=invoice_id)
    context = {
        'invoice_items': invoice_items,
        'this_invoice': this_invoice,
    }
    return render(request, 'Sales/invoice_items.html', context)


from django.conf.urls import url
from . import views

app_name = "Sales"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Invoice/New/$', views.new_invoice, name='new_invoice'),
    url(r'^Invoice/Reverse/$', views.reverse, name='reverse'),
    url(r'^Invoice/Reverse/Item$', views.reverse_item, name='reverse_item'),
    url(r'^Invoice/(?P<invoice_id>[0-9]+)/$', views.edit_invoice, name='edit_invoice'),
    url(r'^Invoice/(?P<invoice_id>[0-9]+)/Add/$', views.add_item_to_sales_invoice, name='add_item'),
    url(r'^Invoice/(?P<invoice_id>[0-9]+)/Save/$', views.save_invoice, name='save_invoice'),
    url(r'^Invoice/(?P<invoice_id>[0-9]+)/Pay/$', views.invoice_payment, name='invoice_payment'),
    url(r'^Invoice/(?P<invoice_id>[0-9]+)/Cancel/$', views.cancel_invoice, name='cancel_invoice'),
    url(r'^Invoice/(?P<invoice_id>[0-9]+)/Items/$', views.get_invoice_items, name='get_invoice_items'),
    url(r'^Reports/$', views.sales_reports, name='sales_reports'),
    url(r'^Reports/Customer/$', views.customer_reports, name='customer_reports'),
    url(r'^Reports/Product/$', views.product_reports, name='product_reports'),
    url(r'^Reports/Invoice/$', views.invoice_reports, name='invoice_reports'),

]

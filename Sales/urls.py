from django.conf.urls import url
from . import views

app_name = "Sales"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Invoice/New/$', views.new_invoice, name='new_invoice'),
    url(r'^Invoice/(?P<invoice_id>[0-9]+)/$', views.edit_invoice, name='edit_invoice'),
    url(r'^Invoice/(?P<invoice_id>[0-9]+)/Add/', views.add_item_to_sales_invoice, name='add_item'),

]
from django.conf.urls import url
from . import views

app_name = "Stock"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_stock/(?P<product_id>[0-9]+)/$', views.get_stock, name='get_stock'),

]

from django.conf.urls import url
from . import views

app_name = "System_Setting"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Default/$', views.default_system_setting, name='system_setting'),
    url(r'^Products/$', views.product_setting, name='product_setting'),
    url(r'^Employee/$', views.employee_management, name='employee'),

]
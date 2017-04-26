from django.conf.urls import url
from . import views

app_name = "System_Setting"
urlpatterns = [
    url(r'^$', views.index, name='index'),

]
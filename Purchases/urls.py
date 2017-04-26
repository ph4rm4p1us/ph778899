from django.conf.urls import url
from . import views

app_name = "Purchases"
urlpatterns = [
    url(r'^$', views.index, name='index'),

]
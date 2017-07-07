from django.conf.urls import url
from . import views

app_name = "Branches"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Add/$', views.add_branch, name='add_branch'),
    url(r'^List/$', views.list_branches, name='list_branches'),

]
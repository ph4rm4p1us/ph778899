from django.conf.urls import url
from . import views

app_name = "Accounts"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Banks/$', views.bank_accounts, name='bank_accounts'),
    url(r'^Banks/Add/$', views.add_bank_account, name='add_bank_account'),
    url(r'^Banks/Edit/(?P<account_id>[0-9]+)/$', views.edit_bank_account, name='edit_bank_account'),
    url(r'^Banks/Delete/(?P<account_id>[0-9]+)/$', views.delete_bank_account, name='delete_bank_account'),
    url(r'^Expense/Category/$', views.expense_category, name='expense_category'),
    url(r'^Expense/Category/Add/$', views.add_expense_category, name='add_expense_category'),
    url(r'^Expense/Category/Edit/(?P<account_id>[0-9]+)/$', views.edit_expense_category, name='edit_expense_category'),
    url(r'^Expense/Category/Delete/(?P<account_id>[0-9]+)/$', views.delete_expense_category, name='delete_expense_category'),
]
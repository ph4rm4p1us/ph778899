from django.conf.urls import url
from . import views

app_name = "Accounts"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Treasury/$', views.treasury, name='treasury'),
    url(r'^Treasury/Add/$', views.add_treasury, name='add_treasury'),
    url(r'^Treasury/Edit/(?P<pk>[0-9]+)/$', views.edit_treasury, name='edit_treasury'),
    url(r'^Treasury/Delete/(?P<pk>[0-9]+)/$', views.delete_treasury, name='delete_treasury'),
    url(r'^Banks/$', views.bank_accounts, name='bank_accounts'),
    url(r'^Banks/Add/$', views.add_bank_account, name='add_bank_account'),
    url(r'^Banks/Edit/(?P<account_id>[0-9]+)/$', views.edit_bank_account, name='edit_bank_account'),
    url(r'^Banks/Delete/(?P<account_id>[0-9]+)/$', views.delete_bank_account, name='delete_bank_account'),
    url(r'^Expense/$', views.expenses, name='expense'),
    url(r'^Expense/Add/$', views.add_expense, name='add_expense'),
    url(r'^Expense/Edit/(?P<pk>[0-9]+)/$', views.edit_expense, name='edit_expense'),
    url(r'^Expense/Delete/(?P<pk>[0-9]+)/$', views.delete_expense, name='delete_expense'),
    url(r'^Expense/Category/$', views.expense_category, name='expense_category'),
    url(r'^Expense/Category/Add/$', views.add_expense_category, name='add_expense_category'),
    url(r'^Expense/Category/Edit/(?P<account_id>[0-9]+)/$', views.edit_expense_category, name='edit_expense_category'),
    url(r'^Expense/Category/Delete/(?P<account_id>[0-9]+)/$', views.delete_expense_category,
        name='delete_expense_category'),
]

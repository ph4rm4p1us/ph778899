from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'Accounts/accountsHome.html', context)
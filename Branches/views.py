from django.shortcuts import render
from .forms import *
from Core.views import *


# Create your views here.
def index(request):
    context = {}
    return render(request, 'Branches/branchesHome.html', context)


def add_branch(request):
    form = AddBranch(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        branch = form.save(commit=False)
        branch.pharmacy = get_pharmacy(request)
        branch.save()
        success_message = "تم إضافة فرع " + branch.name + " بنجاح!"
        context.update({"success_message": success_message})
    return render(request, 'Branches/add_branch.html', context)


def list_branches(request):
    branches = Branches.objects.filter(pharmacy=get_pharmacy(request))
    context = {
        'branches': branches
    }
    return render(request, 'Branches/list_branches.html', context)

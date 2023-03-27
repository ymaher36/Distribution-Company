from django.http import JsonResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import render
from django.urls import reverse

from human_resources.user_details.models import User
from inventory.branches.forms import AddBranch
from inventory.branches.models import Branch, BranchPhoneNumber
from inventory.products.forms import AddEmployeesToBranch
from locations.addresses.models import Location


def branches_settings(request):
    return render(request, "inventory/branches/branches_settings.html")


def add_branch(request):
    addresses = Location.objects.all()
    form = AddBranch()
    if request.POST:
        form = AddBranch(request.POST)
        if form.is_valid():
            branch_name = form.cleaned_data.get('branch_name_input')
            branch_phone_number = form.cleaned_data.get('branch_phone_number_input')
            address_id = form.cleaned_data.get('address_choose_input')
            address = addresses.filter(id=address_id).first()

            branch = Branch(
                name=branch_name,
                location=address,
            )
            branch.save()
            branch_pn = BranchPhoneNumber(
                branch=branch,
                phone_number=branch_phone_number
            )
            branch_pn.save()
    context = {
        'addresses': addresses,
        'form': form
    }
    return render(request, "inventory/branches/add_branch.html", context)


def add_employee_to_branch(request):
    branches = Branch.objects.all()
    employees = User.objects.all()
    employees_no_branch = employees.filter(branch__isnull=True)
    if request.GET:
        branch_id = request.GET.get('branch_name_choose_input')
        employees = employees.filter(branch_id=branch_id)
    elif request.POST:
        form = AddEmployeesToBranch(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data.get('employee_name_choose_input')
            branch_id = form.cleaned_data.get('branch_name_choose_input2')
            user = User.objects.filter(id=employee_id).first()
            user.branch_id = branch_id
            user.save()
    context = {
        'branches': branches,
        'employees': employees,
        'employees_no_branch': employees_no_branch,
    }
    return render(request, "inventory/branches/add_employee_to_branch.html", context)


# def delete_employee_from_branch(request):



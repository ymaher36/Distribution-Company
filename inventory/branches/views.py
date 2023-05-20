from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import render

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
    employees = get_user_model().objects.filter(is_superuser=False, is_active=True)
    employees_no_branch = employees.filter(user_details__branch__isnull=True, is_superuser=False, is_active=True)
    if request.GET:
        branch_id = request.GET.get('branch_name_choose_input')
        employees = employees.filter(user_details__branch_id=branch_id)
    elif request.POST:
        form = AddEmployeesToBranch(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data.get('employee_name_choose_input')
            branch_id = form.cleaned_data.get('branch_name_choose_input2')
            user_details = get_user_model().objects.filter(id=employee_id).first().user_details
            user_details.branch.add(branch_id)
    context = {
        'branches': branches,
        'employees': employees,
        'employees_no_branch': employees_no_branch,
    }
    return render(request, "inventory/branches/add_employee_to_branch.html", context)

# def delete_employee_from_branch(request):

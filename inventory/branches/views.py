from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import render
from django.urls import reverse

from inventory.branches.forms import AddBranch, EditBranch, AddBranchPhoneNumber
from inventory.branches.models import Branch, PhoneNumber
from inventory.products.forms import AddEmployeesToBranch
from locations.addresses.models import Location


def branches_settings(request):
    return render(request, "inventory/branches/branches_settings.html")


def add_branch(request):
    branches = Branch.active.all()
    addresses = Location.objects.all()
    form = AddBranch()
    if request.POST:
        form = AddBranch(request.POST)
        if form.is_valid():
            branch_name = form.cleaned_data.get('branch_name_input')
            number = form.cleaned_data.get('branch_phone_number_input')
            address_id = form.cleaned_data.get('address_choose_input')
            address = addresses.filter(id=address_id).first()
            phone_number = PhoneNumber(number=number)
            branch = Branch(
                name=branch_name,
                location=address,
            )
            branch.save()
            phone_number.save()
            branch.phone_number.add(phone_number)
    context = {
        'addresses': addresses,
        'branches': branches,
        'form': form
    }
    return render(request, "inventory/branches/add_branch.html", context)


def edit_branch(request):
    if request.method == "POST":
        form = EditBranch(request.POST)
        if form.is_valid():
            branch_id = form.cleaned_data.get('edited_branch_id_input')
            name = form.cleaned_data.get('edited_branch_name_input')
            address_id = form.cleaned_data.get('edited_address_choose_input')
            branch = Branch.objects.filter(id=branch_id).first()
            branch.name = name
            branch.location_id = address_id
            branch.save()
        elif form.errors:
            print(form.errors)
        else:
            print("ERROR")
    reverse_url = reverse("inventory:add_branch")
    return HttpResponseRedirect(reverse_url)


def add_branch_phone_number(request):
    if request.method == "POST":
        form = AddBranchPhoneNumber(request.POST)
        if form.is_valid():
            branch_id = form.cleaned_data.get('edited_branch_id_input')
            number = form.cleaned_data.get('edited_branch_phone_number_input')
            phone_number = PhoneNumber(number=number)
            phone_number.save()
            branch = Branch.objects.filter(id=branch_id).first()
            branch.phone_number.add(phone_number)
        elif form.errors:
            print(form.errors)
        else:
            print("ERROR")
    reverse_url = reverse("inventory:add_branch")
    return HttpResponseRedirect(reverse_url)


def add_employee_to_branch(request):
    branches = Branch.active.all()
    employees = get_user_model().objects.filter(is_superuser=False, is_active=True, user_details__is_deleted=False)
    employees_no_branch = employees.filter(user_details__branch__isnull=True, is_superuser=False, is_active=True,
                                           user_details__is_deleted=False)
    branch_employees = []
    if request.GET:
        branch_id = request.GET.get('branch_name_choose_input')
        print(branch_id)
        branch_employees = employees.filter(user_details__branch=branch_id)
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
        'branch_employees': branch_employees,
    }
    return render(request, "inventory/branches/add_employee_to_branch.html", context)

# def delete_employee_from_branch(request):

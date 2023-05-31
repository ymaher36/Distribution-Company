from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from inventory.branches.models import Branch
from locations.addresses.models import Location
from purchases.suppliers.forms import AddSupplier, AddSupplierType, EditSupplier, AddSupplierPhoneNumber, \
    AddSupplierToBranch
from purchases.suppliers.models import SupplierType, Supplier, PhoneNumber


def search_supplier(request):
    context = {}
    return render(request, 'purchases/suppliers/search.html', context)


def add_supplier(request):
    branches = Branch.objects.all()
    addresses = Location.objects.all()
    types = SupplierType.objects.all()
    latest_suppliers = Supplier.objects.all().order_by('-created_at')[:10]
    if request.POST:
        form = AddSupplier(request.POST)
        if form.is_valid():
            supplier_name = form.cleaned_data.get('supplier_name_input')
            branch_id = form.cleaned_data.get('branch_name_choose_input')
            supplier_type_id = form.cleaned_data.get('supplier_type_choose_input')
            address_id = form.cleaned_data.get('address_choose_input')
            number = form.cleaned_data.get('supplier_phone_number_input')
            supplier = Supplier(
                name=supplier_name,
                type_id=supplier_type_id
            )
            phone_number = PhoneNumber(number=number)
            phone_number.save()
            supplier.save()
            supplier.branch.add(branch_id)
            supplier.phone_number.add(phone_number)
            supplier.location.add(address_id)

    context = {
        "branches": branches,
        "addresses": addresses,
        "types": types,
        "latest_suppliers": latest_suppliers,
    }
    return render(request, 'purchases/suppliers/add_supplier.html', context)


def edit_supplier(request):
    if request.method == "POST":
        form = EditSupplier(request.POST)
        if form.is_valid():
            supplier_id = form.cleaned_data.get("edited_supplier_id_input")
            supplier_name = form.cleaned_data.get("edited_supplier_name_input")
            type_id = form.cleaned_data.get("edited_supplier_type_choose_input")
            supplier = Supplier.objects.filter(id=supplier_id).first()
            supplier.name = supplier_name
            supplier.type_id = type_id
            supplier.save()
        elif form.errors:
            print(form.errors)
        else:
            print("ERROR")
    reverse_url = reverse("purchases:add_supplier")
    return HttpResponseRedirect(reverse_url)


def add_supplier_to_branch(request):
    if request.method == "POST":
        form = AddSupplierToBranch(request.POST)
        if form.is_valid():
            supplier_id = form.cleaned_data.get('edited_supplier_id_input')
            branch_id = form.cleaned_data.get('edited_branch_name_choose_input')
            supplier = Supplier.objects.filter(id=supplier_id).first()
            if not supplier.branch.filter(id=branch_id).exists():
                supplier.branch.add(branch_id)
        elif form.errors:
            print(form.errors)
        else:
            print("ERROR")
    reverse_url = reverse("purchases:add_supplier")
    return HttpResponseRedirect(reverse_url)


def add_supplier_phone_number(request):
    if request.method == "POST":
        form = AddSupplierPhoneNumber(request.POST)
        if form.is_valid():
            supplier_id = form.cleaned_data.get("edited_supplier_id_input")
            number = form.cleaned_data.get("edited_supplier_phone_number_input")
            phone_number = PhoneNumber(number=number)
            phone_number.save()
            supplier = Supplier.objects.filter(id=supplier_id).first()
            supplier.phone_number.add(phone_number)
        elif form.errors:
            print(form.errors)
        else:
            print("ERROR")
    reverse_url = reverse("purchases:add_supplier")
    return HttpResponseRedirect(reverse_url)


def supplier_others(request):
    supplier_types = SupplierType.objects.all()
    context = {
        "supplier_types": supplier_types
    }
    return render(request, 'purchases/suppliers/others.html', context)


def add_type(request):
    if request.POST:
        form = AddSupplierType(request.POST)
        if form.is_valid():
            supplier_type_name = form.cleaned_data.get('supplier_type_name_input')
            supplier_type = SupplierType(
                name=supplier_type_name
            )
            supplier_type.save()
    redirect_url = reverse('purchases:supplier_others')
    return HttpResponseRedirect(redirect_url)


def get_branch_suppliers(request):
    select2_data_list = []
    branch_id = request.GET.get('branch_id')
    suppliers = Supplier.objects.filter(branch_id=branch_id)
    for supplier in suppliers:
        select2_data_list.append({
            'id': supplier.id,
            'name': supplier.type.name + ": " + supplier.name,
        })
    return JsonResponse(select2_data_list, safe=False)

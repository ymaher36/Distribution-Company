from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from inventory.branches.models import Branch
from locations.addresses.models import Location
from purchases.suppliers.forms import AddSupplier, AddSupplierType
from purchases.suppliers.models import SupplierType, Supplier


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
            supplier = Supplier(
                name=supplier_name,
                branch_id=branch_id,
                type_id=supplier_type_id
            )
            supplier.save()
            supplier.location.add(address_id)

    context = {
        "branches": branches,
        "addresses": addresses,
        "types": types,
        "latest_suppliers": latest_suppliers,
    }
    return render(request, 'purchases/suppliers/add_supplier.html', context)


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
            print(form.cleaned_data)
            supplier_type_name = form.cleaned_data.get('supplier_type_name_input')
            supplier_type = SupplierType(
                name=supplier_type_name
            )
            supplier_type.save()
    redirect_url = reverse('purchases:supplier_others')
    return HttpResponseRedirect(redirect_url)

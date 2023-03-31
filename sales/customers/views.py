from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from inventory.branches.models import Branch
from locations.addresses.models import Location
from sales.customers.forms import AddCustomerType, AddCustomer
from sales.models import CustomerType, Customer


def search_customer(request):
    context = {}
    return render(request, 'sales/customers/search.html', context)


def add_customer(request):
    branches = Branch.objects.all()
    addresses = Location.objects.all()
    types = CustomerType.objects.all()
    latest_customers = Customer.objects.all().order_by('-created_at')[:10]
    if request.POST:
        form = AddCustomer(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data.get('customer_name_input')
            branch_id = form.cleaned_data.get('branch_name_choose_input')
            customer_type_id = form.cleaned_data.get('customer_type_choose_input')
            address_id = form.cleaned_data.get('address_choose_input')
            customer = Customer(
                name=customer_name,
                branch_id=branch_id,
                type_id=customer_type_id
            )
            customer.save()
            customer.location.add(address_id)
    context = {
        'branches': branches,
        'addresses': addresses,
        'types': types,
        'latest_customers': latest_customers,
    }
    return render(request, 'sales/customers/add_customer.html', context)


def customer_others(request):
    customer_types = CustomerType.objects.all()
    context = {
        "customer_types": customer_types,
    }
    return render(request, 'sales/customers/others.html', context)


def add_type(request):
    if request.POST:
        form = AddCustomerType(request.POST)
        if form.is_valid():
            customer_type_name_input = form.cleaned_data.get('customer_type_name_input')
            customer_type = CustomerType(
                name=customer_type_name_input
            )
            customer_type.save()
    redirect_url = reverse('sales:customer_others')
    return HttpResponseRedirect(redirect_url)


def get_branch_customers(request):
    select2_data_list = []
    branch_id = request.GET.get('branch_id')
    customers = Customer.objects.filter(branch_id=branch_id)
    for customer in customers:
        select2_data_list.append({
            'id': customer.id,
            'name': customer.type.name + " -- " + customer.name,
        })
    return JsonResponse(select2_data_list, safe=False)

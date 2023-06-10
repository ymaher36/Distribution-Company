from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from inventory.branches.models import Branch
from locations.addresses.models import Location
from sales.customers.forms import AddCustomerType, AddCustomer, EditCustomer, AddCustomerPhoneNumber, AddCustomerBranch
from sales.customers.models import CustomerType, Customer, PhoneNumber


def search_customer(request):
    context = {}
    return render(request, 'sales/customers/search.html', context)


def add_customer(request):
    branches = Branch.active.all()
    addresses = Location.objects.all()
    types = CustomerType.objects.all()
    latest_customers = Customer.active.all().order_by('-created_at')[:10]
    if request.POST:
        form = AddCustomer(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data.get('customer_name_input')
            branch_id = form.cleaned_data.get('branch_name_choose_input')
            customer_type_id = form.cleaned_data.get('customer_type_choose_input')
            address_id = form.cleaned_data.get('address_choose_input')
            number = form.cleaned_data.get('customer_phone_number_input')
            customer = Customer(
                name=customer_name,
                type_id=customer_type_id
            )
            phone_number = PhoneNumber(number=number)
            phone_number.save()
            customer.save()
            customer.branch.add(branch_id)
            customer.phone_number.add(phone_number)
            customer.location.add(address_id)
    context = {
        'branches': branches,
        'addresses': addresses,
        'types': types,
        'latest_customers': latest_customers,
    }
    return render(request, 'sales/customers/add_customer.html', context)


def edit_customer(request):
    if request.method == "POST":
        form = EditCustomer(request.POST)
        if form.is_valid():
            customer_id = form.cleaned_data.get('edited_customer_id_input')
            customer_name = form.cleaned_data.get('edited_customer_name_input')
            type_id = form.cleaned_data.get('edited_customer_type_choose_input')

            customer = Customer.objects.filter(id=customer_id).first()
            customer.name = customer_name
            customer.type_id = type_id
            customer.save()
        elif form.errors:
            print(form.errors)
        else:
            print("ERROR")
    reverse_url = reverse("sales:add_customer")
    return HttpResponseRedirect(reverse_url)


def add_customer_branch(request):
    if request.method == "POST":
        form = AddCustomerBranch(request.POST)
        if form.is_valid():
            customer_id = form.cleaned_data.get('edited_customer_id_input')
            branch_id = form.cleaned_data.get('edited_branch_name_choose_input')
            customer = Customer.objects.filter(id=customer_id).first()
            if not customer.branch.filter(id=branch_id).exists():
                customer.branch.add(branch_id)
        elif form.errors:
            print(form.errors)
        else:
            print("ERROR")
    reverse_url = reverse("sales:add_customer")
    return HttpResponseRedirect(reverse_url)


def add_customer_phone_number(request):
    if request.method == "POST":
        form = AddCustomerPhoneNumber(request.POST)
        if form.is_valid():
            customer_id = form.cleaned_data.get('edited_customer_id_input')
            number = form.cleaned_data.get('edited_customer_phone_number_input')
            customer = Customer.objects.filter(id=customer_id).first()
            phone_number = PhoneNumber(number=number)
            phone_number.save()
            customer.phone_number.add(phone_number)
        elif form.errors:
            print(form.errors)
        else:
            print("ERROR")
    reverse_url = reverse("sales:add_customer")
    return HttpResponseRedirect(reverse_url)


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


# ToDo handle soft-delete in all project
def get_branch_customers(request):
    select2_data_list = []
    branch_id = request.GET.get('branch_id')
    customers = Customer.active.filter(branch_id=branch_id)
    for customer in customers:
        select2_data_list.append({
            'id': customer.id,
            'name': customer.type.name + " -- " + customer.name,
        })
    return JsonResponse(select2_data_list, safe=False)

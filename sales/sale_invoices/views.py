import datetime

from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models.functions import Coalesce
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.db.models import F, Subquery, OuterRef
from psycopg2 import DatabaseError

from inventory.branches.models import Branch
from purchases.purchase_invoices.models import PurchaseProduct
from sales.customers.models import Customer
from sales.sale_invoices.forms import AddSaleChannel, EditPriceListForm, GetBranchForm, AddSaleForm
from sales.sale_invoices.models import PricingList, SellingChannel, Order, OrderProducts


def search_sale_invoice(request):
    context = {}
    return render(request, 'sales/sale_invoices/search.html', context)


def add_sale_invoice(request):
    branches = Branch.objects.all() if request.user.is_superuser else request.user.user_details.branch.all
    check = False
    context = {
        'branches': branches,
        'check': check,
    }
    if request.GET:
        get_branch_form = GetBranchForm(request.GET)
        check = True
        if get_branch_form.is_valid():
            branch_id = get_branch_form.cleaned_data.get('branch_choose_input')
            branch = Branch.objects.filter(id=branch_id).first()
            customers = branch.customer_set.all()
            sale_channels = SellingChannel.objects.all()
            employees = get_user_model().objects.filter(user_details__branch__id=branch_id)
            products = PurchaseProduct.objects.filter(purchase__branch_id=branch_id,
                                                      sold_amount__lt=F('quantity')).annotate(
                selling_price=Subquery(
                    PricingList.objects.filter(product_id=OuterRef('id'), end_date__isnull=True).values(
                        'selling_price')[:1]))
            context["products"] = products
            context["branch"] = branch
            context["customers"] = customers
            context["sale_channels"] = sale_channels
            context["employees"] = employees
            context["check"] = check
        else:
            print(get_branch_form.errors)
    elif request.POST:
        products_form_names = list(request.POST.keys())[7:-1]
        invoice_form = AddSaleForm(request.POST)
        products_form_values_check = []
        products_form_values = []
        for form_input in request.POST.items():
            if form_input[0] in products_form_names:
                products_form_values_check.append(True if form_input[1] != '' else False)
                products_form_values.append(form_input[1])

        if invoice_form.is_valid() and len(products_form_names) % 3 == 0 and all(products_form_values_check):
            products_dict = {}
            total_price = 0
            total_amount_boxes = 0
            branch_id = invoice_form.cleaned_data.get('branch_name_input')
            customer_id = invoice_form.cleaned_data.get('customer_choose_input')
            sale_channel_id = invoice_form.cleaned_data.get('sale_channel_choose_input')
            created_by_employee_id = invoice_form.cleaned_data.get('created_by_employee_choose_input')
            receiving_date = invoice_form.cleaned_data.get('receiving_date_input')
            note = invoice_form.cleaned_data.get('note_input')
            discount = invoice_form.cleaned_data.get('discount_input')
            for i in range(0, len(products_form_values), 3):
                products_dict['product' + str(i // 3)] = products_form_values[i:i + 3]
            for product in products_dict.values():
                total_price += int(product[1]) * int(product[2])
                total_amount_boxes += int(product[2])
            total_price -= discount
            sale_invoice = Order(
                customer_id=customer_id,
                branch_id=branch_id,
                selling_channel_id=sale_channel_id,
                total_price=total_price,
                discount=discount,
                receiving_date=receiving_date,
                amount_of_boxes=total_amount_boxes,
                created_by_id=created_by_employee_id,
                note=note,
                state='sold'
            )
            try:
                with transaction.atomic():
                    sale_invoice.save()
                    for product in products_dict.values():
                        product_id = product[0]
                        price = product[1]
                        quantity = product[2]

                        purchase_product = OrderProducts(
                            order_id=sale_invoice.id,
                            product_id=product_id,
                            price=price,
                            quantity=quantity
                        )
                        purchase_product.save()
            except DatabaseError as e:
                print(e)
        elif invoice_form.errors:
            print(invoice_form.errors)
        else:
            print("Error")
    return render(request, 'sales/sale_invoices/add_invoice.html', context)


def price_list(request):
    products = PurchaseProduct.objects.filter(sold_amount__lt=F('quantity')).order_by('product')
    branches = Branch.objects.all()
    if request.POST:
        form = EditPriceListForm(request.POST)
        if form.is_valid():
            selected_products = form.cleaned_data.get('product_choose_input')
            price = form.cleaned_data.get('price_input')
            for product in selected_products:
                product_pricelist = PricingList.objects.filter(product_id=product, end_date__isnull=True).first()
                if product_pricelist:
                    product_pricelist.end_date = datetime.datetime.now()
                    product_pricelist.save()
                product_pricelist = PricingList(
                    product_id=product,
                    selling_price=price
                )
                product_pricelist.save()
        else:
            print(form.errors)
    context = {
        'products': products,
        'branches': branches,
    }
    return render(request, 'sales/sale_invoices/price_list.html', context)


def get_price_list_by_branch(request):
    table_data_list = []
    branch_id = request.GET.get('branch_id')
    if branch_id == "all":
        products = PricingList.objects.filter(end_date__isnull=True).order_by('product__product')
    else:
        products = PricingList.objects.filter(end_date__isnull=True, product__purchase__branch=branch_id).order_by(
            'product__product')
    for product in products:
        table_data_list.append(
            {'product_name': product.product.product.name, 'expire_date': product.product.expire_date,
             'price': product.selling_price})

    return JsonResponse(table_data_list, safe=False)


def sale_invoice_others(request):
    sale_channels = SellingChannel.objects.all()
    context = {
        'sale_channels': sale_channels,
    }
    return render(request, 'sales/sale_invoices/others.html', context)


def add_sale_channel(request):
    if request.POST:
        form = AddSaleChannel(request.POST)
        if form.is_valid():
            sale_channel_name_input = form.cleaned_data.get('sale_channel_name_input')
            sale_channel = SellingChannel(
                name=sale_channel_name_input
            )
            sale_channel.save()
    redirect_url = reverse('sales:sale_invoice_others')
    return HttpResponseRedirect(redirect_url)


def get_product_price(request):
    product_id = request.GET.get('product_id')
    price = PricingList.objects.filter(product=product_id, end_date__isnull=True).first().selling_price
    return JsonResponse(price, safe=False)

def get_invoice_by_branch(request):
    select2_data_list = []
    branch_id = request.GET.get('branch_id')
    invoices = Order.objects.filter(branch=branch_id)
    for invoice in invoices:
        select2_data_list.append({
            'id': invoice.id,
            'name': "العميل: " + invoice.customer.name + ", السعر: " + str(
                invoice.total_price) + ", بيع عن طريق: " + invoice.selling_channel.name + ", تاريخ الأستلام: " +
                    str(invoice.receiving_date)
        })
    return JsonResponse(select2_data_list, safe=False)

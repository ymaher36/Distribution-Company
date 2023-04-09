import datetime

from django.db.models.functions import Coalesce
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.db.models import F, Subquery, OuterRef

from human_resources.user_details.models import User
from inventory.branches.models import Branch
from purchases.purchase_invoices.models import PurchaseProduct
from sales.customers.models import Customer
from sales.sale_invoices.forms import AddSaleChannel, EditPriceListForm, GetBranchForm, AddSaleForm
from sales.sale_invoices.models import PricingList, SellingChannel


def search_sale_invoice(request):
    context = {}
    return render(request, 'sales/sale_invoices/search.html', context)


def add_sale_invoice(request):
    branches = Branch.objects.all()
    context = {
        'branches': branches,
    }
    if request.GET:
        get_branch_form = GetBranchForm(request.GET)
        if get_branch_form.is_valid():
            branch_id = get_branch_form.cleaned_data.get('branch_choose_input')
            branch = branches.filter(id=branch_id).first()
            customers = Customer.objects.filter(branch_id=branch_id)
            sale_channels = SellingChannel.objects.all()
            employees = User.objects.filter(branch_id=branch_id)
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
        else:
            print(get_branch_form.errors)
    elif request.POST:
        add_sale_form = AddSaleForm(request.POST)
        if add_sale_form.is_valid():
            print(add_sale_form.cleaned_data)

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
        products = PricingList.objects.filter(end_date__isnull=True, product__purchase__branch_id=branch_id).order_by(
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

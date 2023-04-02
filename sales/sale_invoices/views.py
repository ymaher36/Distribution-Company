import datetime

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.db.models import F

from inventory.branches.models import Branch
from purchases.purchase_invoices.models import PurchaseProduct
from sales.sale_invoices.forms import AddSaleChannel, EditPriceListForm
from sales.sale_invoices.models import PricingList, SellingChannel


def search_sale_invoice(request):
    context = {}
    return render(request, 'sales/sale_invoices/search.html', context)


def add_sale_invoice(request):
    context = {}
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
        print(product)
        table_data_list.append(
            {'product_name': product.product.product.name, 'expire_date': product.product.expire_date,
             'price': product.selling_price})
    print(table_data_list)

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

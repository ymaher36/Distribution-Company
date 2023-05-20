from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from psycopg2 import DatabaseError

from inventory.branches.models import Branch
from inventory.products.models import Product
from purchases.purchase_invoices.forms import AddPurchaseChannel, AddPurchaseForm
from purchases.purchase_invoices.models import PurchasingChannel, Purchase, PurchaseProduct


# @login_required()
def search_purchase_invoice(request):
    context = {}
    return render(request, 'purchases/purchase_invoices/search.html', context)


def add_purchase_invoice(request):
    branches = Branch.objects.all()
    products = Product.objects.all()
    purchase_channel = PurchasingChannel.objects.all()

    if request.POST:
        products_form_names = list(request.POST.keys())[6:]
        invoice_form = AddPurchaseForm(request.POST)
        products_form_values_check = []
        products_form_values = []
        for form_input in request.POST.items():
            if form_input[0] in products_form_names:
                products_form_values_check.append(True if form_input[1] != '' else False)
                products_form_values.append(form_input[1])
        if invoice_form.is_valid() and len(products_form_names) % 4 == 0 and all(products_form_values_check):
            products_dict = {}
            total_price = 0
            total_amount_boxes = 0
            branch_id = invoice_form.cleaned_data.get('branch_name_choose_input')
            supplier_id = invoice_form.cleaned_data.get('supplier_choose_input')
            purchase_channel_id = invoice_form.cleaned_data.get('purchase_channel_choose_input')
            note = invoice_form.cleaned_data.get('note_input')
            receiving_date = invoice_form.cleaned_data.get('receiving_date_input')
            for i in range(0, len(products_form_values), 4):
                products_dict['product' + str(i // 4)] = products_form_values[i:i + 4]
            for product in products_dict.values():
                total_price += int(product[2])*int(product[3])
                total_amount_boxes += int(product[3])
            purchase_invoice = Purchase(
                branch_id=branch_id,
                seller_id=supplier_id,
                purchase_channel_id=purchase_channel_id,
                receiving_date=receiving_date,
                note=note,
                total_price=total_price,
                amount_of_boxes=total_amount_boxes,
                amount_of_brands=0,
                amount_of_types=0,
                type="purchase"
            )
            try:
                with transaction.atomic():
                    purchase_invoice.save()
                    for product in products_dict.values():
                        product_id = product[0]
                        expire_date = product[1]
                        price = product[2]
                        quantity = product[3]
                        purchase_product = PurchaseProduct(
                            purchase_id=purchase_invoice.id,
                            product_id=product_id,
                            expire_date=expire_date,
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
    context = {
        'branches': branches,
        'products': products,
        'purchase_channel': purchase_channel,
    }
    return render(request, 'purchases/purchase_invoices/add_invoice.html', context)


def purchase_invoice_others(request):
    purchase_channels = PurchasingChannel.objects.all()
    context = {
        "purchase_channels": purchase_channels
    }
    return render(request, 'purchases/purchase_invoices/others.html', context)


def add_purchase_channel(request):
    if request.POST:
        form = AddPurchaseChannel(request.POST)
        if form.is_valid():
            purchase_channel_name = form.cleaned_data.get('purchase_channel_name_input')
            purchase_channel = PurchasingChannel(
                name=purchase_channel_name
            )
            purchase_channel.save()
    redirect_url = reverse('purchases:purchase_invoice_others')
    return HttpResponseRedirect(redirect_url)

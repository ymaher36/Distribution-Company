from django.shortcuts import render


def search_customer(request):
    context = {}
    return render(request, 'sales/sale_invoices/search.html', context)


def add_customer(request):
    context = {}
    return render(request, 'sales/sale_invoices/add_invoice.html', context)

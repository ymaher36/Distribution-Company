from django.shortcuts import render


def search_purchase_invoice(request):
    context = {}
    return render(request, 'purchases/purchase_invoices/search.html', context)
def add_purchase_invoice(request):
    context = {}
    return render(request, 'purchases/purchase_invoices/add_invoice.html', context)
from django.urls import path

from purchases.purchase_invoices import views

urlpatterns = [
    path("", views.search_purchase_invoice, name="search_purchase_invoice"),
    path("add-purchase-invoice", views.add_purchase_invoice, name="add_purchase_invoice")
]

from django.urls import path

from purchases.purchase_invoices import views

urlpatterns = [
    path("", views.search_purchase_invoice, name="search_purchase_invoice"),
    path("add-purchase-invoice/", views.add_purchase_invoice, name="add_purchase_invoice"),
    path("purchase-invoice-others/", views.purchase_invoice_others, name="purchase_invoice_others"),
    path("add-purchase-channel/", views.add_purchase_channel, name="add_purchase_channel"),
    path("get-invoice-by-branch/", views.get_invoice_by_branch, name="get_invoice_by_branch"),
]

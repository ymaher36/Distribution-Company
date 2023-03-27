from django.urls import path, include

app_name = "purchases"

urlpatterns = [
    path("purchase-invoices/", include('purchases.purchase_invoices.urls')),
    path("suppliers/", include('purchases.suppliers.urls')),
]

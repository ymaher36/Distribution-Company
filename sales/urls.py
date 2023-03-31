from django.urls import path, include

app_name = "sales"

urlpatterns = [
    path("sale-invoices/", include('sales.sale_invoices.urls')),
    path("customers/", include('sales.customers.urls')),
]

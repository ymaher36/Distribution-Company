from django.urls import path

from sales.sale_invoices import views

urlpatterns = [
    path('', views.search_sale_invoice, name='search_sale_invoice'),
    path('add-sale-invoice/', views.add_sale_invoice, name='add_sale_invoice'),
]

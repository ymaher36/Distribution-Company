from django.urls import path

from sales.sale_invoices import views

urlpatterns = [
    path('', views.search_sale_invoice, name='search_sale_invoice'),
    path('add-sale-invoice/', views.add_sale_invoice, name='add_sale_invoice'),
    path('price-list/', views.price_list, name='price_list'),
    path('get-price-list-by-branch/', views.get_price_list_by_branch, name='get_price_list_by_branch'),
    path('sale-invoice-others/', views.sale_invoice_others, name='sale_invoice_others'),
    path('add-sale-channel/', views.add_sale_channel, name='add_sale_channel'),
    path('get-product-price/', views.get_product_price, name='get_product_price'),
    path('get-invoice-by-branch/', views.get_invoice_by_branch, name='get_invoice_by_branch'),

]

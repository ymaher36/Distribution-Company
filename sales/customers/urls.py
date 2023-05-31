from django.urls import path

from sales.customers import views

urlpatterns = [
    path('', views.search_customer, name='search_customer'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('edit-customer/', views.edit_customer, name='edit_customer'),
    path('add-customer-branch/', views.add_customer_branch, name='add_customer_branch'),
    path('add-customer-phone-number/', views.add_customer_phone_number, name='add_customer_phone_number'),
    path('customer-others/', views.customer_others, name='customer_others'),
    path("add-customer-type/", views.add_type, name='add_type'),

]

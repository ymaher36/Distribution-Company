from django.urls import path

from sales.customers import views

urlpatterns = [
    path('', views.search_customer, name='search_customer'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('customer-others/', views.customer_others, name='customer_others'),
    path("add-customer-type/", views.add_type, name='add_type'),

]

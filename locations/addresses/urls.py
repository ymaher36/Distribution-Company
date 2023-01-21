from django.urls import path

from locations.addresses.views import view_addresses, add_address

urlpatterns = [
    path('', view_addresses, name='view_addresses'),
    path('add/', add_address, name='add_address'),
]
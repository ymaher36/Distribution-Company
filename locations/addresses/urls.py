from django.urls import path

from locations.addresses.views import view_addresses, add_address, get_district_related_to_governorate

urlpatterns = [
    path('', view_addresses, name='view_addresses'),
    path('add/', add_address, name='add_address'),
    path('get_district_related_to_governorate/', get_district_related_to_governorate,
         name='get_district_related_to_governorate')
]

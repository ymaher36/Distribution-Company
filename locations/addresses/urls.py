from django.urls import path

from locations.addresses.views import view_addresses, add_address, get_district_related_to_governorate, delete_address, \
    get_address_data, edit_address

urlpatterns = [
    path('', view_addresses, name='view_addresses'),
    path('add/', add_address, name='add_address'),
    path('delete-address/<uuid:location_id>/', delete_address, name='delete_address'),
    path('edit-address/', edit_address, name='edit_address'),
    path('get-district-related-to-governorate/', get_district_related_to_governorate,
         name='get_district_related_to_governorate'),
    path("get-address-data/", get_address_data, name='get_address_data')

]

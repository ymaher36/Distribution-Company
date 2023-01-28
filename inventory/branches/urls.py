from django.urls import path

from inventory.branches import views

urlpatterns = [
    path("", views.branches_settings, name='branches_settings'),
    path("add_branch/", views.add_branch, name='add_branch'),
    path("add_user_to_branch/", views.add_user_to_branch, name='add_user_to_branch'),
    path("get_address_data/", views.get_address_data, name='get_address_data')
]

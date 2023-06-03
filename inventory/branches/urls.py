from django.urls import path

from inventory.branches import views

urlpatterns = [
    path("", views.branches_settings, name='branches_settings'),
    path("add-branch/", views.add_branch, name='add_branch'),
    path("edit-branch/", views.edit_branch, name='edit_branch'),
    path("add-branch-phone-number/", views.add_branch_phone_number, name='add_branch_phone_number'),
    path("add-employee-to-branch/", views.add_employee_to_branch, name='add_employee_to_branch'),
]

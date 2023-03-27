from django.urls import path

from inventory.branches import views

urlpatterns = [
    path("", views.branches_settings, name='branches_settings'),
    path("add-branch/", views.add_branch, name='add_branch'),
    path("add-employee-to-branch/", views.add_employee_to_branch, name='add_employee_to_branch'),
]

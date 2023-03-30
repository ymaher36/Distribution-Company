from django.urls import path

from purchases.suppliers import views

urlpatterns = [
    path("", views.search_supplier, name='search_supplier'),
    path("add-supplier/", views.add_supplier, name='add_supplier'),
    path("supplier-others/", views.supplier_others, name='supplier_others'),
    path("add-supplier-type/", views.add_type, name='add_type'),
    path("get-branch-suppliers/", views.get_branch_suppliers, name='get_branch_suppliers'),
]

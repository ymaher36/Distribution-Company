from django.urls import path

from inventory.products import views

urlpatterns = [
    path("", views.search_products, name='search_products'),
    path("add-products/", views.add_products, name='add_products'),
    path("delete-product/<uuid:product_id>/", views.delete_product, name='delete_product'),
    path("edit-product/", views.edit_product, name='edit_product'),
    path("brands/", views.brands, name='brands'),
    path("add-brand/", views.add_brand, name='add_brand'),
    path("delete-brand/<uuid:brand_id>/", views.delete_brand, name='delete_brand'),
    path("edit-brand/", views.edit_brand, name='edit_brand'),
    path("add-category/", views.add_category, name='add_category'),
    path("delete-category/<uuid:category_id>/", views.delete_category, name='delete_category'),
    path("edit-category/", views.edit_category, name='edit_category'),

]

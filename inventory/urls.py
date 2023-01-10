from django.urls import path

from inventory import views

urlpatterns = [
    path("products/", views.products, name='products'),
    path("edit_products/", views.edit_products, name='edit_products'),
    path("brands/", views.brands, name='brands'),
    path("add_brand/", views.add_brand, name='add_brand'),
    path("delete_brand/<uuid:brand_id>/", views.delete_brand, name='delete_brand'),
    path("add_category/", views.add_category, name='add_category'),
    path("delete_category/<uuid:category_id>/", views.delete_category, name='delete_category'),
    path("warehouse/", views.warehouse, name='warehouse')
]

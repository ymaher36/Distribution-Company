from django.urls import path

from inventory.products import views

urlpatterns = [
    path("search/", views.search_products, name='search_products'),
    path("add_products/", views.add_products, name='add_products'),
    path("delete_product/<uuid:product_id>/", views.delete_product, name='delete_product'),
    path("brands/", views.brands, name='brands'),
    path("add_brand/", views.add_brand, name='add_brand'),
    path("delete_brand/<uuid:brand_id>/", views.delete_brand, name='delete_brand'),
    path("add_category/", views.add_category, name='add_category'),
    path("delete_category/<uuid:category_id>/", views.delete_category, name='delete_category'),
]

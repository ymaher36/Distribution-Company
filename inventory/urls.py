from django.urls import path, include

app_name = "inventory"
urlpatterns = [
    path('products/', include('inventory.products.urls')),
    path('branches/', include('inventory.branches.urls')),
]

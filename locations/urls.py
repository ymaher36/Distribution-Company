from django.urls import path, include

app_name = "locations"

urlpatterns = [
    path('address/', include('locations.addresses.urls'))
]

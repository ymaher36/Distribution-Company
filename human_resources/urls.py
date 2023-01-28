from django.urls import path, include

app_name = "human_resources"
urlpatterns = [
    path("users/", include('human_resources.user_details.urls'))
]

from django.urls import path

from human_resources.user_details import views

urlpatterns = [
    path('', views.user_details, name='users.details')
]

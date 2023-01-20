from django.urls import path

from inventory.branches import views

urlpatterns = [

    path("", views.branches_settings, name='branches_settings')
]

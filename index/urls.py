from django.urls import path

from index import views

urlpatterns = [
    path('', views.home_page, name='home_page')
]

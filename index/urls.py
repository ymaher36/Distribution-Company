from django.urls import path, include

from index import views

urlpatterns = [
    path('', views.home_page, name='home_page')
]

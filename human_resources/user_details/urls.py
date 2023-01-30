from django.urls import path

from human_resources.user_details import views

urlpatterns = [
    path('', views.user_details, name='users_details'),
    path('add_user/', views.add_user, name='add_user'),
    path('user_accounts/', views.user_accounts, name='user_accounts')
]

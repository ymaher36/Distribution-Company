from django.urls import path

from human_resources.user_details import views

urlpatterns = [
    path('', views.user_details, name='users_details'),
    path('add_user/', views.add_user, name='add_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('user_accounts/', views.user_accounts, name='user_accounts'),
    path('other_settings/', views.other_settings, name='other_settings'),
    path('add_role/', views.add_role, name='add_role'),
    path('delete_role/<uuid:role_id>/', views.delete_role, name='delete_role')
]

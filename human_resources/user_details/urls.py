from django.urls import path

from human_resources.user_details import views

urlpatterns = [
    path('', views.user_details, name='users_details'),
    path('add-user/', views.add_user, name='add_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('edit-user/', views.edit_user, name='edit_user'),
    path('edit-account/', views.edit_account, name='edit_account'),
    path('user-accounts/', views.user_accounts, name='user_accounts'),
    path('other-settings/', views.other_settings, name='other_settings'),
    path('add-role/', views.add_role, name='add_role'),
    path('delete-role/<uuid:role_id>/', views.delete_role, name='delete_role')
]

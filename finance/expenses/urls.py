from django.urls import path

from finance.expenses import views

urlpatterns = [
    path("", views.search_expenses, name='search_expenses'),
    path("add-expense", views.add_expenses, name='add_expenses'),
    # path("edit-expense", views.edit_expenses, name='edit_expenses'),
    # path("delete-expense", views.delete_expenses, name='delete_expenses'),
    path("expense-others", views.expense_others, name='expense_others'),
]

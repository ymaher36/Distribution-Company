from django.urls import path, include

app_name = "finance"

urlpatterns = [
    path("expenses/", include('finance.expenses.urls')),
]

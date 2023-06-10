from django.contrib.auth import get_user_model
from django.shortcuts import render

from finance.expenses.forms import AddExpense
from finance.expenses.models import ExpenseType, Expense
from inventory.branches.models import Branch


def search_expenses(request):
    context = {}
    return render(request, "finance/expenses/seach.html", context)


def add_expenses(request):
    types = ExpenseType.objects.all()
    branches = Branch.active.all() if request.user.is_superuser else request.user.user_details.branch.all
    if request.method == "POST":
        form = AddExpense(request.POST)
        if form.is_valid():
            branch_id = form.cleaned_data.get('branch_choose_input')
            employee_id = form.cleaned_data.get('created_by_input')
            price = form.cleaned_data.get('expense_price_input')
            type_id = form.cleaned_data.get('type_choose_input')
            order_id = form.cleaned_data.get('order_choose_input')
            purchase_id = form.cleaned_data.get('purchase_choose_input')
            other = form.cleaned_data.get('other_input')
            expense = Expense(
                branch_id=branch_id,
                created_by_id=employee_id,
                amount=price,
                type_id=type_id,
                order_id=order_id,
                purchase_id=purchase_id,
                note=other
            )
            expense.save()
        elif form.errors:
            print(form.errors)
        else:
            print("ERROR")
    context = {
        'types': types,
        'branches': branches,
    }
    return render(request, "finance/expenses/add_expense.html", context)


def expense_others(request):
    context = {}
    return render(request, "finance/expenses/others.html", context)

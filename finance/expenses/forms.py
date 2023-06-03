from django import forms


class AddExpense(forms.Form):
    branch_choose_input = forms.UUIDField(
        required=True
    )
    created_by_input = forms.CharField(
        required=True
    )
    expense_price_input = forms.DecimalField(
        required=True,
        min_value=0
    )
    other_input = forms.CharField(
        required=True
    )
    type_choose_input = forms.UUIDField(
        required=False
    )
    order_choose_input = forms.UUIDField(
        required=False
    )
    purchase_choose_input = forms.UUIDField(
        required=False
    )

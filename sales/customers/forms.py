from django import forms

class AddCustomer(forms.Form):
    customer_name_input = forms.CharField(
        required=True
    )
    branch_name_choose_input = forms.CharField(
        required=True
    )
    customer_type_choose_input = forms.CharField(
        required=True
    )
    address_choose_input = forms.CharField(
        required=True
    )
class AddCustomerType(forms.Form):
    customer_type_name_input = forms.CharField(
        required=True
    )

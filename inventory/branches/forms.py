from django import forms


class AddBranch(forms.Form):
    branch_name_input = forms.CharField(
        required=True
    )
    branch_phone_number_input = forms.CharField(
        required=True
    )
    address_choose_input = forms.CharField(
        required=True
    )

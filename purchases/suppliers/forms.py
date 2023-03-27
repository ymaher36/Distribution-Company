from django import forms


class AddSupplier(forms.Form):
    supplier_name_input = forms.CharField(
        required=True
    )
    branch_name_choose_input = forms.CharField(
        required=True
    )
    supplier_type_choose_input = forms.CharField(
        required=True
    )
    address_choose_input = forms.CharField(
        required=True
    )


class AddSupplierType(forms.Form):
    supplier_type_name_input = forms.CharField(
        required=True
    )

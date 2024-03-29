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
    supplier_phone_number_input = forms.CharField(
        required=True
    )


class EditSupplier(forms.Form):
    edited_supplier_id_input = forms.UUIDField(
        required=True
    )
    edited_supplier_type_choose_input = forms.UUIDField(
        required=True
    )
    edited_supplier_name_input = forms.CharField(
        required=True
    )


class AddSupplierPhoneNumber(forms.Form):
    edited_supplier_id_input = forms.UUIDField(
        required=True
    )
    edited_supplier_phone_number_input = forms.CharField(
        required=True
    )


class AddSupplierToBranch(forms.Form):
    edited_supplier_id_input = forms.UUIDField(
        required=True
    )
    edited_branch_name_choose_input = forms.UUIDField(
        required=True
    )


class AddSupplierType(forms.Form):
    supplier_type_name_input = forms.CharField(
        required=True
    )

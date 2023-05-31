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
    customer_phone_number_input = forms.CharField(
        required=True
    )
    address_choose_input = forms.CharField(
        required=True
    )


class EditCustomer(forms.Form):
    edited_customer_id_input = forms.UUIDField(
        required=True
    )
    edited_customer_type_choose_input = forms.UUIDField(
        required=True
    )
    edited_customer_name_input = forms.CharField(
        required=True
    )


class AddCustomerBranch(forms.Form):
    edited_customer_id_input = forms.UUIDField(
        required=True
    )
    edited_branch_name_choose_input = forms.UUIDField(
        required=True
    )


class AddCustomerPhoneNumber(forms.Form):
    edited_customer_id_input = forms.UUIDField(
        required=True
    )
    edited_customer_phone_number_input = forms.CharField(
        required=True
    )


class AddCustomerType(forms.Form):
    customer_type_name_input = forms.CharField(
        required=True
    )

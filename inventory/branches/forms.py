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


class EditBranch(forms.Form):
    edited_branch_id_input = forms.UUIDField(
        required=True
    )
    edited_branch_name_input = forms.CharField(
        required=True
    )
    edited_address_choose_input = forms.UUIDField(
        required=True
    )


class AddBranchPhoneNumber(forms.Form):
    edited_branch_id_input = forms.UUIDField(
        required=True
    )
    edited_branch_phone_number_input = forms.CharField(
        required=True
    )

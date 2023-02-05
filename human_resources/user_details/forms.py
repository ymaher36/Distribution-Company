from django import forms


class AddNewUserForm(forms.Form):
    user_name_input = forms.CharField(
        required=True
    )
    national_id_input = forms.CharField(
        required=True
    )
    role_choose_input = forms.CharField(
        required=True
    )
    user_phone_number_input = forms.CharField(
        required=True
    )
    birthdate_input = forms.DateField(
        required=True
    )
    start_work_date_input = forms.DateField(
        required=False
    )
    address_choose_input = forms.CharField(
        required=True
    )
    gender_choose_input = forms.CharField(
        required=True
    )


class AddRole(forms.Form):
    role_name_input = forms.CharField(
        required=True
    )

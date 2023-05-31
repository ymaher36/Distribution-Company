from django import forms


class AddNewUserForm(forms.Form):
    user_name_input = forms.CharField(
        required=True
    )
    national_id_input = forms.CharField(
        required=True,
        max_length=14,
        min_length=14
    )
    role_choose_input = forms.CharField(
        required=True
    )
    user_phone_number_input = forms.CharField(
        required=True,
        max_length=11
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


class EditUser(forms.Form):
    edited_user_id_input = forms.IntegerField(
        required=True
    )
    edited_user_details_id_input = forms.UUIDField(
        required=True
    )
    edited_user_name_input = forms.CharField(
        required=True
    )
    edited_national_id_input = forms.CharField(
        max_length=14,
        min_length=14,
        required=True
    )
    edited_role_choose_input = forms.UUIDField(
        required=True
    )
    edited_birthdate_input = forms.DateField(
        required=True
    )
    edited_gender_choose_input = forms.CharField(
        required=True
    )
    edited_start_work_date_input = forms.DateField(
        required=True
    )


class EditAccount(forms.Form):
    edited_user_id_input = forms.IntegerField(
        required=True
    )
    password_input = forms.CharField(
        required=True
    )
    username_input = forms.CharField(
        required=True
    )


class AddRole(forms.Form):
    role_name_input = forms.CharField(
        required=True
    )

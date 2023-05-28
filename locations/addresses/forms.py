from django import forms


class AddAddress(forms.Form):
    governorate_choose_input = forms.CharField(
        required=True
    )
    district_choose_input = forms.CharField(
        required=True
    )
    other_input = forms.CharField(
        required=False
    )
    street_name_input = forms.CharField(
        required=True
    )


class EditAddress(forms.Form):
    edited_address_id_input = forms.UUIDField(
        required=True
    )
    edited_governorate_choose_input = forms.UUIDField(
        required=True
    )
    edited_district_choose_input = forms.UUIDField(
        required=True
    )
    edited_street_name_input = forms.CharField(
        required=True
    )
    edited_other_input = forms.CharField(
        required=False
    )

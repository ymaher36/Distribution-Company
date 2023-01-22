from django import forms


class AddAddress(forms.Form):
    street_name_input = forms.CharField(
        required=True
    )
    district_id_input = forms.UUIDField(
        required=True
    )
    other_input = forms.CharField(
        required=True
    )

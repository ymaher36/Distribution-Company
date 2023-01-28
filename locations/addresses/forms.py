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

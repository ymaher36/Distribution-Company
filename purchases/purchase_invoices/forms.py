from django import forms


class AddPurchaseForm(forms.Form):
    branch_name_choose_input = forms.CharField(
        required=True
    )
    supplier_choose_input = forms.CharField(
        required=True
    )
    purchase_channel_choose_input = forms.CharField(
        required=True
    )
    note_input = forms.CharField(
        required=False
    )
    receiving_date_input = forms.DateField(
        required=True
    )


class AddPurchaseProductForm(forms.Form):
    product_choose_input = forms.CharField(
        required=True
    )
    price_input = forms.CharField(
        required=True
    )
    quantity_input = forms.CharField(
        required=True
    )
    expire_date_input = forms.DateField(
        required=True
    )


class AddPurchaseChannel(forms.Form):
    purchase_channel_name_input = forms.CharField(
        required=True
    )

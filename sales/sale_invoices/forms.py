from django import forms
from django.core.exceptions import ValidationError


class GetBranchForm(forms.Form):
    branch_choose_input = forms.CharField(
        required=True
    )


class AddSaleForm(forms.Form):
    branch_name_input = forms.CharField(
        required=True
    )
    customer_choose_input = forms.CharField(
        required=True
    )
    sale_channel_choose_input = forms.CharField(
        required=True
    )
    created_by_employee_choose_input = forms.CharField(
        required=True
    )
    receiving_date_input = forms.DateField(
        required=True,
        input_formats=['%Y-%m-%d'],
    )
    note_input = forms.CharField(
        required=False
    )


class CustomMultipleChoiceField(forms.MultipleChoiceField):
    """This field is a MultipleChoiceField designed to override the validation method of a default MultipleChoiceField"""

    def validate(self, value):
        if len(value) == 0:
            raise ValidationError(self.error_messages["required"], code="required")
        return value


class EditPriceListForm(forms.Form):
    product_choose_input = CustomMultipleChoiceField(
        required=True
    )
    price_input = forms.DecimalField(
        required=True
    )


class AddSaleChannel(forms.Form):
    sale_channel_name_input = forms.CharField(
        required=True
    )

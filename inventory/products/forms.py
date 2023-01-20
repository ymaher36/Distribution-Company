from django import forms


class addBrandForm(forms.Form):
    brand_name_input = forms.CharField(
        required=True
    )


class addCategoryForm(forms.Form):
    category_name_input = forms.CharField(
        required=True
    )


class addProductForm(forms.Form):
    product_name_input = forms.CharField(
        required=True
    )
    brand_choose_input = forms.CharField(
        required=True
    )
    category_choose_input = forms.CharField(
        required=True
    )



class searchProductForm(forms.Form):
    product_search_name_input = forms.CharField()
    brand_search_choose_input = forms.CharField()
    category_search_choose_input = forms.CharField()


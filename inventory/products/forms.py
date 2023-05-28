from django import forms


class AddBrandForm(forms.Form):
    brand_name_input = forms.CharField(
        required=True
    )


class AddCategoryForm(forms.Form):
    category_name_input = forms.CharField(
        required=True
    )


class EditCategoryForm(forms.Form):
    edited_category_id_input = forms.UUIDField(
        required=True
    )
    edited_category_name_input = forms.CharField(
        required=True
    )


class EditBrandForm(forms.Form):
    edited_brand_id_input = forms.UUIDField(
        required=True
    )
    edited_brand_name_input = forms.CharField(
        required=True
    )


class EditProductForm(forms.Form):
    edited_product_id_input = forms.UUIDField(
        required=True
    )
    edited_product_name_input = forms.CharField(
        required=True
    )
    edited_brand_search_choose_input = forms.UUIDField(
        required=True
    )
    edited_category_search_choose_input = forms.UUIDField(
        required=True
    )


class AddProductForm(forms.Form):
    product_name_input = forms.CharField(
        required=True
    )
    brand_choose_input = forms.UUIDField(
        required=True
    )
    category_choose_input = forms.UUIDField(
        required=True
    )


class AddEmployeesToBranch(forms.Form):
    branch_name_choose_input2 = forms.CharField()
    employee_name_choose_input = forms.CharField()


class SearchProductForm(forms.Form):
    product_search_name_input = forms.CharField()
    brand_search_choose_input = forms.CharField()
    category_search_choose_input = forms.CharField()

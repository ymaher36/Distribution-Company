from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from inventory.products.forms import AddBrandForm, AddCategoryForm, AddProductForm, SearchProductForm, EditProductForm, \
    EditBrandForm, EditCategoryForm
from inventory.products.models import Brand, ProductCategory, Product


def search_products(request):
    brands = Brand.objects.all()
    categories = ProductCategory.objects.all()
    products = Product.objects.all().order_by("-created_at")

    if request.GET:
        form = SearchProductForm(request.GET)
        if form.is_valid():
            product_name = form.cleaned_data['product_search_name_input']
            brand = form.cleaned_data['product_search_name_input']
            product_name = form.cleaned_data['product_search_name_input']
            # products = products.
    context = {
        'brands': brands,
        'products': products,
        'categories': categories,

    }
    return render(request, 'inventory/products/products.html', context)


def add_products(request):
    brands = Brand.objects.all()
    categories = ProductCategory.objects.all()
    products = Product.objects.all().order_by("-created_at")[:10]

    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name_input']
            category_id = pk = form.cleaned_data['category_choose_input']
            brand_id = form.cleaned_data['brand_choose_input']
            product = Product(category_id=category_id,
                              brand_id=brand_id,
                              name=product_name)
            product.save()
    context = {
        'brands': brands,
        'products': products,
        'categories': categories
    }
    return render(request, 'inventory/products/add_products.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    reverse_url = reverse("inventory:add_products")
    return HttpResponseRedirect(reverse_url)


def edit_product(request):
    if request.method == "POST":
        form = EditProductForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data.get('edited_product_id_input')
            product_name = form.cleaned_data.get('edited_product_name_input')
            product_brand_id = form.cleaned_data.get('edited_brand_search_choose_input')
            product_category_id = form.cleaned_data.get('edited_category_search_choose_input')
            product = Product.objects.filter(id=product_id).first()
            product.name = product_name
            product.brand_id = product_brand_id
            product.category_id = product_category_id
            product.save()
        elif form.errors:
            print(form.errors)
        else:
            print("error")
    reverse_url = reverse("inventory:search_products")
    return HttpResponseRedirect(reverse_url)


def brands(request):
    brands = Brand.objects.all()
    product_categories = ProductCategory.objects.all()
    context = {
        "brands": brands,
        "cateories": product_categories
    }
    return render(request, 'inventory/products/brand.html', context)


def add_brand(request):
    if request.method == "POST":
        form = AddBrandForm(request.POST)
        if form.is_valid():
            brand_name = form.cleaned_data['brand_name_input']
            brand = Brand(name=brand_name)
            brand.save()
    reverse_url = reverse("inventory:brands")
    return HttpResponseRedirect(reverse_url)


def delete_brand(request, brand_id):
    brand = Brand.objects.filter(id=brand_id).first()
    brand.delete()
    reverse_url = reverse("inventory:brands")
    return HttpResponseRedirect(reverse_url)


def edit_brand(request):
    if request.method == "POST":
        form = EditBrandForm(request.POST)
        if form.is_valid():
            brand_id = form.cleaned_data.get('edited_brand_id_input')
            brand_name = form.cleaned_data.get('edited_brand_name_input')
            brand = Brand.objects.filter(id=brand_id).first()
            brand.name = brand_name
            brand.save()
        elif form.errors:
            print(form.errors)
        else:
            print("Error")
    reverse_url = reverse("inventory:brands")
    return HttpResponseRedirect(reverse_url)


def add_category(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category_name_input']
            category = ProductCategory(name=category_name)
            category.save()
    reverse_url = reverse("inventory:brands")
    return HttpResponseRedirect(reverse_url)


def delete_category(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    category.delete()
    reverse_url = reverse("inventory:brands")
    return HttpResponseRedirect(reverse_url)


def edit_category(request):
    if request.method == "POST":
        form = EditCategoryForm(request.POST)
        if form.is_valid():
            category_id = form.cleaned_data.get("edited_category_id_input")
            category_name = form.cleaned_data.get("edited_category_name_input")
            category = ProductCategory.objects.filter(id=category_id).first()
            category.name = category_name
            category.save()
        elif form.errors:
            print(form.errors)
        else:
            print("Error")
    reverse_url = reverse("inventory:brands")
    return HttpResponseRedirect(reverse_url)

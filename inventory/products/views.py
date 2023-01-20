from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from inventory.products.forms import addBrandForm, addCategoryForm, addProductForm, searchProductForm
from inventory.products.models import Brand, ProductCategory, Product


def search_products(request):
    brands = Brand.objects.all()
    categories = ProductCategory.objects.all()
    products = Product.objects.all().order_by("-created_at")
    context = {
        'brands': brands,
        'products': products,
        'categories': categories
    }
    if request.method == "GET":
        form = searchProductForm(request.GET)
        if form.is_valid():
            product_name = form.cleaned_data['product_search_name_input']
            brand = form.cleaned_data['product_search_name_input']
            product_name = form.cleaned_data['product_search_name_input']

    return render(request, 'inventory/products/products.html', context)


def add_products(request):
    brands = Brand.objects.all()
    categories = ProductCategory.objects.all()
    products = Product.objects.all().order_by("-created_at")[:10]

    if request.method == "POST":
        form = addProductForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name_input']
            category = ProductCategory.objects.filter(pk=form.cleaned_data['category_choose_input']).first()
            brand = Brand.objects.filter(name=form.cleaned_data['brand_choose_input']).first()
            product = Product(product_category=category,
                              product_brand=brand,
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
        form = addBrandForm(request.POST)
        if form.is_valid():
            brand_name = form.cleaned_data['brand_name_input']
            brand = Brand(name=brand_name)
            brand.save()
    reverse_url = reverse("inventory:brands")
    return HttpResponseRedirect(reverse_url)


def delete_brand(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    brand.delete()
    reverse_url = reverse("inventory:brands")
    return HttpResponseRedirect(reverse_url)


def add_category(request):
    if request.method == "POST":
        form = addCategoryForm(request.POST)
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

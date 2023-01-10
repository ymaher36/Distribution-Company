from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from inventory.models import Brand, ProductCategory


def warehouse(request):
    return None


def products(request):
    return render(request, 'inventory/products.html')


def edit_products(request):
    return render(request, 'inventory/edit_products.html')


def brands(request):
    brands = Brand.objects.all()
    product_categories = ProductCategory.objects.all()
    context = {
        "brands": brands,
        'cateories': product_categories
    }
    return render(request, 'inventory/brand.html', context)


def add_brand(request):
    if request.method == "POST":
        brand_name = request.POST.get('brand-name-input')
        brand = Brand(name=brand_name)
        brand.save()
    reverse_url = reverse("brands")
    return HttpResponseRedirect(reverse_url)


def delete_brand(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    print(brand_id)
    brand.delete()
    reverse_url = reverse("brands")
    return HttpResponseRedirect(reverse_url)


def add_category(request):
    if request.method == "POST":
        category_name = request.POST.get('category-name-input')
        category = ProductCategory(name=category_name)
        category.save()
    reverse_url = reverse("brands")
    return HttpResponseRedirect(reverse_url)


def delete_category(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    print(category_id)
    category.delete()
    reverse_url = reverse("brands")
    return HttpResponseRedirect(reverse_url)

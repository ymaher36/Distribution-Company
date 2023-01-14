from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from inventory.models import Brand, ProductCategory, Product


def warehouse(request):
    return None


def products(request):
    return render(request, 'inventory/products.html')


def add_products(request):
    brands = Brand.objects.all()
    categories = ProductCategory.objects.all()
    products = Product.objects.all().order_by("-created_at")[:10]
    context = {
        'brands': brands,
        'products': products,
        'categories': categories
    }
    if request.method == "POST":
        category = ProductCategory.objects.filter(pk=request.POST.get('category_choose_input')).first()
        brand = Brand.objects.filter(name=request.POST.get('brand_choose_input')).first()
        product = Product(product_category=category,
                          product_brand=brand,
                          expire_at=request.POST.get('expire_at_date_input'),
                          name=request.POST.get('product-name-input'))
        product.save()
    return render(request, 'inventory/add_products.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    reverse_url = reverse("add_products")
    return HttpResponseRedirect(reverse_url)


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

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from locations.addresses.models import Location


def branches_settings(request):
    return render(request, "inventory/branches/branches_settings.html")


def add_branch(request):
    addresses = Location.objects.all()
    context = {
        'addresses': addresses
    }
    return render(request, "inventory/branches/add_branch.html", context)


def add_user_to_branch(request):
    return render(request, "inventory/branches/add_user_to_branch.html")


def get_address_data(request):
    address_id = request.GET.get('address_id')
    address = Location.objects.filter(id=address_id).first()
    response_data = {
        'governorate': address.district.governorate.name,
        'district': address.district.name_ar,
        'street': address.street,
        'other': address.other
    }
    return JsonResponse(response_data, safe=False)


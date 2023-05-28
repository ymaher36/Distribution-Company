from django.db.models import Subquery, OuterRef
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from locations.addresses.forms import AddAddress, EditAddress
from locations.addresses.models import Location, Governorate, District


# Create your views here.

def view_addresses(request):
    return render(request, 'locations/addresses/view_addresses.html')


def add_address(request):
    latest_addresses = Location.objects.all().annotate(
        governorate=Subquery(Governorate.objects.filter(district__id=OuterRef('district_id')).values('name')[:1]),
        governorate_id=Subquery(Governorate.objects.filter(district__id=OuterRef('district_id')).values('id')[:1]),
    ).order_by('-id')[:10]
    governorates = Governorate.objects.all()
    if request.method == 'POST':
        form = AddAddress(request.POST)
        if form.is_valid():
            street = form.cleaned_data['street_name_input']
            district_id = form.cleaned_data['district_choose_input']
            other = form.cleaned_data['other_input']
            location = Location(street=street, district_id=district_id, other=other)
            location.save()
    context = {
        'latest_addresses': latest_addresses,
        'governorates': governorates,
    }
    return render(request, 'locations/addresses/add_address.html', context)


def get_district_related_to_governorate(request):
    select2_data_list = []
    governorate_id = request.GET.get('governorate_id')
    districts = District.objects.filter(governorate_id=governorate_id)
    for district in districts:
        select2_data_list.append({'id': district.id, 'name': district.name_ar})
    return JsonResponse(select2_data_list, safe=False)


def delete_address(request, location_id):
    location = Location.objects.filter(pk=location_id).first()
    location.delete()
    reverse_url = reverse('locations:add_address')
    return HttpResponseRedirect(reverse_url)


def edit_address(request):
    if request.method == "POST":
        form = EditAddress(request.POST)
        if form.is_valid():
            address_id = form.cleaned_data.get('edited_address_id_input')
            governorate_id = form.cleaned_data.get('edited_governorate_choose_input')
            district_id = form.cleaned_data.get('edited_district_choose_input')
            street = form.cleaned_data.get('edited_street_name_input')
            other = form.cleaned_data.get('edited_other_input')
            address = Location.objects.filter(id=address_id).first()
            address.district_id = district_id
            address.street = street
            address.other = other
            address.save()
        elif form.errors:
            print(form.errors)
        else:
            print('ERROR')
    reverse_url = reverse("locations:add_address")
    return HttpResponseRedirect(reverse_url)


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

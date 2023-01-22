from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from locations.addresses.forms import AddAddress
from locations.addresses.models import Location, Governorate, District


# Create your views here.

def view_addresses(request):
    return render(request, 'locations/addresses/view_addresses.html')


def add_address(request):
    latest_addresses = Location.objects.all().order_by('-id')[:10]
    governorates = Governorate.objects.all()
    if request.method == 'POST':
        form = AddAddress(request.POST)
        if form.is_valid():
            pass
            # street =
            # district =
            # other =
    context = {
        'latest_addresses': latest_addresses,
        'governorates': governorates,
    }
    return render(request, 'locations/addresses/add_address.html', context)


def get_district_related_to_governorate(request):
    select2_data_list = []
    governorate_id = request.GET.get('governorate_id')
    print(governorate_id)
    districts = District.objects.filter(governorate_id=governorate_id)
    for district in districts:
        select2_data_list.append({'id': district.id, 'name': district.name_ar})
    return JsonResponse(select2_data_list, safe=False)

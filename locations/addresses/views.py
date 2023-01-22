from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from locations.addresses.forms import AddAddress
from locations.addresses.models import Location


# Create your views here.

def view_addresses(request):
    return render(request, 'locations/addresses/view_addresses.html')


def add_address(request):
    latest_addresses = Location.objects.all().order_by('-id')[:10]
    if request.method == 'POST':
        form = AddAddress(request.POST)
        if form.is_valid():
            pass
            # street =
            # district =
            # other =
    return render(request, 'locations/addresses/add_address.html')

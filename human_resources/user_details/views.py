from django.contrib.auth import get_user_model
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from human_resources.user_details.forms import AddNewUserForm, AddRole
from human_resources.user_details.models import UserDetails, Role, PhoneNumber
from locations.addresses.models import Location


def user_details(request):
    context = {

    }
    return render(request, 'human_resources/user_details/user_details.html', context)


def add_user(request):
    latest_users = get_user_model().objects.filter(is_superuser=False, is_active=True).order_by('-date_joined')[:10]
    roles = Role.objects.all()
    addresses = Location.objects.all()
    if request.method == "POST":
        form = AddNewUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['user_name_input']
            national_id = form.cleaned_data['national_id_input']
            role = form.cleaned_data['role_choose_input']
            phone_number = form.cleaned_data['user_phone_number_input']
            birthdate = form.cleaned_data['birthdate_input']
            start_work_date = form.cleaned_data['start_work_date_input']
            home_location = form.cleaned_data['address_choose_input']
            gender = form.cleaned_data['gender_choose_input']
            with transaction.atomic():

                new_user = get_user_model().objects.create_user(username=national_id, first_name=name)
                new_user_phone_number = PhoneNumber(user=new_user, phone_number=phone_number).save()
                new_user_details = UserDetails(user=new_user, national_id=national_id, role_id=role,
                                               birthdate=birthdate,
                                               start_work_date=start_work_date,
                                               home_location_id=home_location,
                                               gender=gender)
                new_user_details.save()
        else:
            print(form.errors)
    context = {
        'latest_users': latest_users,
        'roles': roles,
        'addresses': addresses
    }
    return render(request, 'human_resources/user_details/add_user.html', context)


def delete_user(request, user_id):
    user = get_user_model().objects.filter(id=user_id).first()
    user.is_active = False
    user.save()
    reverse_url = reverse("human_resources:add_user")
    return HttpResponseRedirect(reverse_url)


def user_accounts(request):
    context = {

    }
    return render(request, 'human_resources/user_details/user_accounts.html', context)


def other_settings(request):
    roles = Role.objects.all()

    context = {
        'roles': roles
    }
    return render(request, 'human_resources/user_details/other_settings.html', context)


def add_role(request):
    if request.method == 'POST':
        form = AddRole(request.POST)
        if form.is_valid():
            role_name = form.cleaned_data['role_name_input']
            role = Role(name=role_name).save()
        else:
            print(form.errors)
    reverse_url = reverse("human_resources:other_settings")
    return HttpResponseRedirect(reverse_url)


def delete_role(request, role_id):
    role = Role.objects.filter(id=role_id).first()
    role.delete()
    reverse_url = reverse("human_resources:other_settings")
    return HttpResponseRedirect(reverse_url)

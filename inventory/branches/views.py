from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def branches_settings(request):
    return render(request, "inventory/branches/branches_settings.html")

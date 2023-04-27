from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def home_page(request):
    return render(request, 'index/home_page.html')


def err_page(request, message):
    return render(request, "index/failure.html", {"message": message}, status=400)

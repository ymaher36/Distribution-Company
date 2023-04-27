from django.http import HttpResponseRedirect
from django.urls import reverse


class AuthRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        redirect_url = reverse("account_login")

        if request.path == redirect_url:
            return self.get_response(request)
        if not request.user.is_authenticated:
            return HttpResponseRedirect(redirect_url)
        response = self.get_response(request)
        return response

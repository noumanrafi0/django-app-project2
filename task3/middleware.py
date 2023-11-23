import logging
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import authenticate


logger = logging.getLogger(__name__)


class CustomAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.method == "POST":
            phone_number = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=phone_number, password=password)

            if user is not None:
                request.user = user
            else:
                return HttpResponse(
                    "<h1 style='color: red; text-align: center;'>Access Denied</h1>"
                )

        response = self.get_response(request)
        return response

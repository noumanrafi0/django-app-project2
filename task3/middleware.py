import logging

from django.utils import timezone

logger = logging.getLogger(__name__)


class CustomAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            logger.info("not authenticated")
        else:
            logger.info("authenticated")

        response = self.get_response(request)
        return response


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get user IP and request data
        ip_add = self.get_user_ip(request)
        method = request.method
        url = request.build_absolute_uri()

        # Log the data
        log_info = f"[{timezone.now()}] IP: {ip_add}\
              | Method: {method} | URL: {url}\n"
        self.do_log(log_info)

        # Continue request
        response = self.get_response(request)
        return response

    def get_user_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    def do_log(self, log_info):
        with open("req_info_log.txt", "a") as log_file:
            log_file.write(log_info)

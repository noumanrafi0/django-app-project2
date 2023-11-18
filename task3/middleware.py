import logging

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

# Optional middleware, not necessary if using signal-based handling.
import traceback
import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

class CadmiumMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        self.send_error_to_cadmium(exception, request)

    def send_error_to_cadmium(self, exception, request):
        headers = {
            "Application-ID": getattr(settings, "APPLICATION_ID", ""),
            "CD-Secret": getattr(settings, "CD_SECRET", ""),
            "CD-ID": getattr(settings, "CD_ID", ""),
            "Content-Type": "application/json",
        }

        payload = {
            "error": str(exception),
            "traceback": traceback.format_exc(),
            "url": request.build_absolute_uri(),
            "method": request.method,
        }

        try:
            requests.post(
                "http://localhost:8080",
                json=payload,
                headers=headers,
                timeout=5
            )
        except requests.RequestException as e:
            logger.error(f"Failed to send error to Cadmium server: {e}")

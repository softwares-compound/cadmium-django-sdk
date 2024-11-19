import traceback
import requests
import logging
from django.core.signals import got_request_exception
from django.conf import settings

logger = logging.getLogger(__name__)

def capture_exception(sender, request=None, **kwargs):
    exception = kwargs.get('exception')
    if not exception:
        return

    headers = _get_cadmium_headers()

    payload = {
        "error": str(exception),
        "traceback": traceback.format_exc(),
        "url": request.build_absolute_uri() if request else "N/A",
        "method": request.method if request else "N/A",
    }

    try:
        response = requests.post(
            "http://localhost:8080",
            json=payload,
            headers=headers,
            timeout=5
        )
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Failed to send error to Cadmium server: {e}")

def _get_cadmium_headers():
    return {
        "Application-ID": getattr(settings, "APPLICATION_ID", ""),
        "CD-Secret": getattr(settings, "CD_SECRET", ""),
        "CD-ID": getattr(settings, "CD_ID", ""),
        "Content-Type": "application/json",
    }

got_request_exception.connect(capture_exception)

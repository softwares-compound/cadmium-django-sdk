import traceback
import requests
import logging
import sys
from django.core.signals import got_request_exception
from django.conf import settings

logger = logging.getLogger(__name__)

def capture_exception(sender, request=None, **kwargs):
    # Use sys.exc_info() to get the current exception
    exc_type, exc_value, exc_traceback = sys.exc_info()

    if not exc_value:
        return

    headers = _get_cadmium_headers()

    payload = {
        "error": str(exc_value),
        "traceback": ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback)),
        "url": request.build_absolute_uri() if request else "N/A",
        "method": request.method if request else "N/A",
    }
    
    try:
        response = requests.post(
            "http://43.204.216.93:8080/logs",
            json=payload,
            headers=headers,
            timeout=5
        )
        print(response.text)
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

# Connect the signal to capture unhandled exceptions
got_request_exception.connect(capture_exception)

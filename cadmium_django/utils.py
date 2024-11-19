def initialize():
    import logging
    from django.core.signals import got_request_exception
    from .signals import capture_exception

    from django.conf import settings
    required_settings = ['APPLICATION_ID', 'CD_SECRET', 'CD_ID']
    for setting in required_settings:
        if not hasattr(settings, setting):
            raise ValueError(f"Missing required setting: {setting}")

    got_request_exception.connect(capture_exception)
    logging.info("Cadmium-Django SDK initialized successfully.")

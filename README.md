# Cadmium-Django SDK

This SDK captures and sends errors from your Django application to the Cadmium server.

## Installation

```bash
pip install cadmium-django-sdk
```

## Configuration

Add the following to your `settings.py`:

```python
INSTALLED_APPS += ['cadmium_django']

APPLICATION_ID = "your-application-id"
CD_SECRET = "your-secret"
CD_ID = "your-cd-id"

import cadmium_django
cadmium_django.initialize()
```

## Usage

Once configured, any unhandled exception will automatically be sent to the Cadmium server.

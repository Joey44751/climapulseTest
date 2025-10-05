import os
import sys

sys.path.append("/app")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "refrigerant_app.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

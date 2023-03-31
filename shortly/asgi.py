# SHORTLY by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

import os

from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shortly.settings')
application = get_asgi_application()

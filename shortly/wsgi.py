# SHORTLY by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

import os

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shortly.settings')
application = get_wsgi_application()

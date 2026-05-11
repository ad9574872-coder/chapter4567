import os
import sys

path = '/home/AyushDutta977/chapter4567'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'chapter4567.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

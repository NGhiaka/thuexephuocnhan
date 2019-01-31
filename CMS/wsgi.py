"""
WSGI config for CMS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
 
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #'E:/Website/www/CMS/'
# path = '/home/nghiaka/src/thuexephuocnhan/'
# path = '/var/www/thuexephuocnhan/'

if path not in sys.path:
 sys.path.append(path)
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'CMS.settings'
 
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())


# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CMS.settings")

# application = get_wsgi_application()

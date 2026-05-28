import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crime_typeand_occurrence_prediction.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

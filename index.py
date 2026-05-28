import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, 'Crime_project', 'Crime_Type_and_Occurrence_Prediction1', 'crime_typeand_occurrence_prediction')
sys.path.insert(0, PROJECT_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crime_typeand_occurrence_prediction.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

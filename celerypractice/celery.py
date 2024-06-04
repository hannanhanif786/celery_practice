import os
import time
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerypractice.settings')

app = Celery('celerypractice')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
# app.autodiscover_tasks()

@app.task()
def hello_world():
    time.sleep(30)
    return 'Hello World!'
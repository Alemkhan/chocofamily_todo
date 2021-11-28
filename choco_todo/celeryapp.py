import os
import django

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'choco_todo.settings')
django.setup()

app = Celery('choco_todo',
             broker='redis://127.0.0.1:6379/0',
             backend='redis://127.0.0.1:6379/0'
             )

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

from celery import Celery

import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sales.settings")
app = Celery("sales")
app.config_from_object("django.conf:settings")

app.autodiscover_tasks()

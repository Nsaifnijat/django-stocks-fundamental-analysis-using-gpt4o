from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtimeapp.settings')

app = Celery('realtimeapp')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

#now we schedule a task using beat.

app.conf.beat_schedule = {
        'get_realtime_prices': {

            'task': 'stocks.tasks.fetch_stock_price',
            'schedule': 1.0

        }}
"""
#Ignore this part, not related to this project!
        'get_realtime_stock_gainers_lossers': {

            'task': 'stocks.tasks.fetch_top_gainers_lossers',
            'schedule': 1.0

        }
    """
    




# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

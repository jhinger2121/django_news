from __future__ import absolute_import
import imp

import os
from celery import Celery
from django.conf import settings
from django.apps import apps

from celery import shared_task


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_news_aggregator.settings')
# BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')


app = Celery('django_news_aggregator')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# lambda: [n.name for n in apps.get_app_configs()]
# lambda: settings.INSTALLED_APPS, force=True
# app.conf.broker_url = BASE_REDIS_URL
# app.conf.C_FORCE_ROOT = 1

if __name__ == '__main__':
    app.start()
    
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'sum_two_numbers',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }


# Other Celery settings
app.conf.beat_schedule = {
    'take_every_day_data': {
        'task': 'extract_data',
        'schedule': 30.0,
    },
}




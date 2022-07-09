from __future__ import absolute_import
import imp

import os
from celery import Celery
from django.conf import settings
from django.apps import apps

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_news_aggregator.settings.local')

app = Celery('django_news_aggregator')

            
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()
    
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'take_every_day_data': {
        'task': 'extract_data',
        'schedule': 60 * 60 * 24,
    },
}




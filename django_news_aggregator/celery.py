from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_news_aggregator.settings')
app = Celery('django_news_aggregator')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

    
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# Other Celery settings
app.conf.beat_schedule = {
    'tasks.main': {
        'task': 'tasks.main',
        'schedule': 30.0,
    },
}




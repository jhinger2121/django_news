from __future__ import absolute_import
import imp

import os
from celery import Celery
from django.conf import settings
from django.apps import apps

from celery import shared_task
import ssl

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_news_aggregator.settings')
# BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
key_file = '/tmp/keyfile.key'
cert_file = '/tmp/certfile.crt'
ca_file = '/tmp/CAtmp.pem'


app = Celery('django_news_aggregator')
app.conf.redis_backend_use_ssl = {
                 'ssl_keyfile': key_file, 'ssl_certfile': cert_file,
                 'ssl_ca_certs': ca_file,
                 'ssl_cert_reqs': 'CERT_REQUIRED'
            }


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
        'schedule': 100,
    },
}




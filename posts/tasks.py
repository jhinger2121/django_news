from celery import shared_task
from crawler.html_request import MakeRequest
from crawler.extractors import (
    extract_djangostars, extract_djangotricks, extract_django_project, extract_number_1
)
from .utils import save_to_db

url_list = [
    'https://www.djangoproject.com/weblog/',
    'https://djangostars.com/blog/tag/django-framework/',
    'https://djangotricks.blogspot.com/',
    'https://number1.co.za/category/django-2/',
]

@shared_task(name='tasks.main')
def main():
    for url in url_list:
        request = MakeRequest()
        response = request._get(url)
        print(response.status_code)
        if 'djangostars' in url:
            dj_data = extract_djangostars(response)
            save_to_db(url, dj_data)
        elif 'djangotricks' in url:
            dngo_trks = extract_djangotricks(response)
            save_to_db(url, dngo_trks)
        elif 'djangoproject' in url:
            dngo_pro = extract_django_project(response)
            save_to_db(url, dngo_pro)
        elif 'number1' in url:
            dngo_no_one = extract_number_1(response)
            save_to_db(url, dngo_no_one)

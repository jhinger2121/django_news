from bs4 import BeautifulSoup
from datetime import datetime

from .html_request import MakeRequest

def extract_djangostars(response):
    django_stars_posts = []
    soup = BeautifulSoup(response.content, 'html.parser')

    card_wraper = soup.find_all('div', class_='l-card')
    # print(len(card_wraper))
    for card in card_wraper:
        djangostars_article = {}
        _title = card.find('div', class_='l-card__title')
        if _title:
            title = _title.a.text
            djangostars_article['title'] = title
        else:
            djangostars_article['title'] = ''

        link = _title.a
        if link:
            djangostars_article['link'] = link['href']
        else:
            djangostars_article['link'] = ''

        _tags = card.find_all('a', class_='l-card__tags-link')
        if _tags:
            tags_list = []
            for a_tag in _tags:
                tag = a_tag.text.lower()
                tags_list.append(tag)
            djangostars_article['tags'] = tags_list
        else:
            djangostars_article['tags'] = []

        _visits = card.find('span', class_='count')
        if _visits:
            visits = _visits.text
            djangostars_article['visits'] = visits
        else:
            djangostars_article['visits'] = 0
        
        # fake data
        djangostars_article['post_by'] = ''
        djangostars_article['created_at'] = datetime.now()
        djangostars_article['rating'] = 0
        djangostars_article['comments'] = 0
        django_stars_posts.append(djangostars_article)
    return django_stars_posts

def extract_djangotricks(response):
    djangotricks_post_list = []
    soup = BeautifulSoup(response.content, 'html.parser')

    post_wraper_list = soup.find_all('div', class_='date-outer')
    for post_list in post_wraper_list:
        djangotricks_article = {}
        _title = post_list.find('h3', class_='post-title entry-title')
        if _title:
            title = _title.a.text
            djangotricks_article['title'] = title.strip()

            link = _title.a['href']
            djangotricks_article['link'] = link
        else:
            djangotricks_article['link'] = ''
            djangotricks_article['title'] = ''

        post_footer = post_list.find('div', class_='post-footer')
        post_by = post_footer.find('a', class_='g-profile')
        if post_by:
            djangotricks_article['post_by'] = post_by.span.text.strip()
        else:
            djangotricks_article['post_by'] = ''

        post_lables = post_footer.find('span', class_='post-labels')
        if post_lables:
            tags_list = []
            _tags = post_lables.find_all('a')
            for a_tag in _tags:
                tag = a_tag.text.lower()
                tags_list.append(tag)
            djangotricks_article['tags'] = tags_list
        else:
            djangotricks_article['tags'] = []
        
        created_at = soup.find('h2', class_='date-header')
        if created_at:
            created_at = created_at.span.text
            djangotricks_article['created_at'] = created_at
        else:
            djangotricks_article['created_at'] = datetime.now()

        djangotricks_article['rating'] = 0
        djangotricks_article['comments'] = 0
        djangotricks_article['visits'] = 0

        djangotricks_post_list.append(djangotricks_article)        
    return djangotricks_post_list

def extract_django_project(response):
    djangoProject_list = []
    soup = BeautifulSoup(response.content, 'html.parser')

    newsList = soup.select(".list-news > li")
    for news in newsList:
        newsPost = {}
        _title = news.find('h2').a
        if _title:
            title = _title.text
            newsPost['title'] = title.strip()

            link = _title['href']
            newsPost['link'] = link.strip()
        else:
            newsPost['title'] = ''
            newsPost['link'] = ''
            
        name_n_date = news.select_one("span.meta")
        if name_n_date:
            post_by = name_n_date.strong.text.strip()
            newsPost['post_by'] = post_by.strip()
        
            # _created_at = name_n_date.text
            # created_at = _created_at.replace(post_by, '').replace('Posted', '').replace('by', '').replace('on', '')
            # newsPost['created_at'] = created_at.strip()
        else:
            newsPost['post_by'] = ''

        # fake data
        newsPost['rating'] = 0
        newsPost['comments'] = 0
        newsPost['visits'] = 0
        newsPost['created_at'] = datetime.now()
        djangoProject_list.append(newsPost)
    return djangoProject_list

def extract_number_1(response):
    posts_of_number1 = []
    soup = BeautifulSoup(response.content, 'html.parser')

    post_wraper_list = soup.find_all('div', class_='card')
    for post_list in post_wraper_list:
        a_post_of_number1 = {}
        _title = post_list.find('h1', class_='entry-title')
        if _title:
            title = _title.a.text
            a_post_of_number1['title'] = title.strip()

            link = _title.a['href']
            a_post_of_number1['link'] = link
        else:
            a_post_of_number1['title'] = ''
            a_post_of_number1['link'] = ''

        created_at = post_list.find('time', class_='entry-date published')
        updated_at = post_list.find('time', class_='updated')
        if updated_at:
            updated_at = updated_at['datetime']
            a_post_of_number1['created_at'] = updated_at
        elif created_at:
            created_at = created_at['datetime']
            a_post_of_number1['created_at'] = created_at
        else:
            a_post_of_number1['created_at'] = datetime.now()

        post_by = post_list.find('span', class_='author vcard')
        if post_by:
            post_by = post_by.get_text()
            a_post_of_number1['post_by'] = post_by
        else:
            a_post_of_number1['post_by'] = ''

        tags_wraper = post_list.find('span', class_='cat-links')
        tags = tags_wraper.find_all('a')
        if tags_wraper and tags:
            tags_of_number1 = []
            for a_tag in tags:
                tags_of_number1.append(a_tag.text)
            a_post_of_number1['tags'] = tags_of_number1
        else:
            a_post_of_number1['tags'] = "django"

        a_post_of_number1['rating'] = 0
        a_post_of_number1['comments'] = 0
        a_post_of_number1['visits'] = 0

        posts_of_number1.append(a_post_of_number1)
    return posts_of_number1


# url_list = [
#     # 'https://www.djangoproject.com/weblog/',
#     'https://djangostars.com/blog/tag/django-framework/',
#     # 'https://djangotricks.blogspot.com/',
#     # 'https://number1.co.za/category/django-2/',
# ]

# for url in url_list:
#     request = MakeRequest()
#     response = request._get(url)
#     extract_djangostars(response)

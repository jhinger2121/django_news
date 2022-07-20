from bs4 import BeautifulSoup
from datetime import datetime

from .html_request import MakeRequest
import re

def extract_djangostars(response):
    django_stars_posts = []
    soup = BeautifulSoup(response.content, 'html.parser')

    card_wraper = soup.find_all('div', class_='article_row')
    for card in card_wraper:
        djangostars_article = {}
        _title = card.find('div', class_='title')
        if _title:
            title = _title.a.text
            djangostars_article['title'] = title.strip()
        else:
            djangostars_article['title'] = ''

        link = _title.a
        if link:
            djangostars_article['link'] = link['href']
        else:
            djangostars_article['link'] = ''

        _visits = card.find('div', class_='views')
        if _visits:
            t_visits = re.findall(r'\d+', _visits.text)
            visits = t_visits[0].replace("/", "")

            djangostars_article['visits'] = visits
        else:
            djangostars_article['visits'] = 0

        _post_by = card.find('div', class_='author')
        _post_by = _post_by.find('div', class_='name')
        if _post_by:
            djangostars_article['post_by'] = _post_by.text.strip()
        else:
            djangostars_article['post_by'] = ''

        # fake data
        djangostars_article['created_at'] = datetime.now()
        djangostars_article['rating'] = 0
        djangostars_article['comments'] = 0
        djangostars_article['tags'] = []
        djangostars_article['headline'] = 0

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
        djangotricks_article['headline'] = 0

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
        
        try:
            name_n_date = news.select_one("span.meta")
            if name_n_date:
                post_by = name_n_date.strong.text.strip()
                newsPost['post_by'] = post_by.strip()
            else:
                newsPost['post_by'] = ''
        except:
            post_by = news.find('span', class_="meta")
            if post_by.a:
                newsPost['post_by'] = post_by.a.text
            else:
                newsPost['post_by'] = ''



        if ('www.djangoproject.com/community/blogs/' in response.url):
            newsPost['headline'] = news.div.text[1:-1]
        else:
            _headline = news.p
            if (_headline):
                newsPost['headline'] = _headline.text
            else:
                newsPost['headline'] = ''
        

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

    post_wraper_list = soup.find_all('article', class_='post')
    for post_list in post_wraper_list:
        a_post_of_number1 = {}
        _title = post_list.find('h2', class_='entry-title')
        if _title:
            title = _title.a.text
            a_post_of_number1['title'] = title.strip()

            link = _title.a['href']
            a_post_of_number1['link'] = link
        else:
            a_post_of_number1['title'] = ''
            a_post_of_number1['link'] = ''


        post_by = post_list.find('li', class_='post-author')
        author = post_by.find('span', class_='meta-text')
        if author:
            author = author.get_text()
            if 'By me' in author:
                a_post_of_number1['post_by'] = "Number_1_owner"
        else:
            a_post_of_number1['post_by'] = author

        tags_wraper = post_list.find('div', class_='entry-categories')
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
        a_post_of_number1['headline'] = 0
        a_post_of_number1['created_at'] = datetime.now()


        posts_of_number1.append(a_post_of_number1)
    return posts_of_number1

def extract_justdjango(response):
    justDjango_posts = []
    soup = BeautifulSoup(response.content, 'html.parser')

    post_wraper = soup.find_all('div', class_='flex-col')
    for a_post in post_wraper:
        a_post_obj = {}
        
        title = a_post.find('h3')
        if title or title is not None:
            a_post_obj['title'] = title.a.text
            a_post_obj['link'] = 'https://justdjango.com' + title.a['href']
        else:
            return justDjango_posts

        tag = a_post.find('div', class_='flow-root')
        if tag.text:
            tag_list = []
            tag_list.append(tag.text)
            a_post_obj['tags'] = tag_list
        else:
            a_post_obj['tags'] = []


        headline = a_post.find('p')
        if headline:
            a_post_obj['headline'] = headline.text
        else:
            a_post_obj['headline'] = ''

        _author = a_post.find('ul', class_='author-list')
        author = _author.find('h4')
        if author:
            a_post_obj['post_by'] = author.text
        else:
            a_post_obj['post_by'] = ''

        time = _author.find('time')

        a_post_obj['rating'] = 0
        a_post_obj['comments'] = 0
        a_post_obj['visits'] = 0
        a_post_obj['created_at'] = time['datetime']

        justDjango_posts.append(a_post_obj)
    return justDjango_posts

def extract_djangocentral(response):
    posts = []
    soup = BeautifulSoup(response.content, 'html.parser')

    post_wraper = soup.find_all('li', class_='py-12')
    for a_post in post_wraper:
        a_post_obj = {}
        
        title = a_post.find('h2')
        if title or title is not None:
            try:
                a_post_obj['title'] = title.a.text
                a_post_obj['link'] = 'https://djangocentral.com' + title.a['href']
            except:
                print("Scraper couldn't find the Post")
                return
        else:
            return

        try:
            if a_post.a.span:
                tag_list = []
                tag_list.append(a_post.a.span.text.capitalize())
                a_post_obj['tags'] = tag_list
        except:
            a_post_obj['tags'] = ''
            print("Scraper couldn't find the tags")

        try:
            if a_post.div:
                a_post_obj['headline'] = a_post.div.text
        except:
            a_post_obj['headline'] = ''

        a_post_obj['post_by'] = ''
        a_post_obj['rating'] = 0
        a_post_obj['comments'] = 0
        a_post_obj['visits'] = 0
        a_post_obj['created_at'] = datetime.now()


        posts.append(a_post_obj)
    return posts


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

import imp
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.cache import cache
from .models import Posts, Website
from datetime import datetime, timedelta
from itertools import chain


def homepage(request, tag_name=None):
    if tag_name:
        posts = Posts.objects.filter(tags__name__in=[tag_name])
    else:
        latter_posts = datetime.now() - timedelta(days=7)
        seven_posts = Posts.objects.exclude(created_at__lt=latter_posts).exclude(website__name="Reddit")
        reddit_posts  = Posts.objects.filter(website__name="Reddit")
        posts = list(chain(seven_posts, reddit_posts))
    paginator = Paginator(posts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/posts_01.html', {'posts': page_obj})

def sort_by_website(request, website_name, tag_name=None):
    posts = Posts.objects.filter(website__name=website_name)
    if website_name and tag_name:
       posts = posts.filter(tags__name__in=[tag_name])
    paginator = Paginator(posts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/posts_02.html', {'posts': page_obj, 'website_name': website_name, 'tag_name': tag_name})

def page_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)

    fav_posts_list = cache.get('fav_posts')
    if fav_posts_list is None:
        cache.set('fav_posts', [post])
    else:
        fav_posts_list.append(post)
        cache.set('fav_posts', fav_posts_list)
    return redirect(post.link)

def favourit_posts(request):
    posts = Posts.objects.filter(favourit=True)
    paginator = Paginator(posts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/posts_01.html', {'posts': page_obj})

def read_latter_posts(request):
    posts = Posts.objects.filter(read_latter=True)
    paginator = Paginator(posts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/posts_02.html', {'posts': page_obj})

def favourit_it(request, post_id):
    post = Posts.objects.get(id=post_id)
    post.favourit = True
    post.save()
    return redirect('/')

from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Posts
from datetime import datetime, timedelta

def homepage(request, tag=None):
    if tag:
        posts = Posts.objects.filter(tags__name__in=[tag])
    else:
        latter_posts = datetime.now() - timedelta(days=7)
        posts = Posts.objects.exclude(created_at__lt=latter_posts).exclude(website__name="Reddit")
        reddit_posts  = Posts.objects.filter(website__name="Reddit")
    tags = Posts.tags.all()
    return render(request, 'posts/index.html', {'posts': posts, 'reddit_posts': reddit_posts, 'tags': tags})


def sort_by_site_name(request, site_name, tag=None):
    posts = Posts.objects.filter(website__name=site_name)
    if tag:
        posts = posts.filter(tags__name__in=[tag])
    tags = Posts.tags.all()
    return render(request, 'posts/index.html', {'posts': posts, 'tags': tags, 'site_name': site_name})

def favourit_posts(request):
    posts = Posts.objects.filter(favourit=True)
    return render(request, 'posts/index.html', {'posts': posts})

def read_latter_posts(request):
    posts = Posts.objects.filter(read_latter=True)
    return render(request, 'posts/index.html', {'posts': posts})

def favourit_it(request, post_id):
    post = Posts.objects.get(id=post_id)
    post.favourit = True
    post.save()
    return redirect('/')
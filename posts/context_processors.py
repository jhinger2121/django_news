from .models import Posts, Website
from django.core.cache import cache

def get_websites_name(request):
    return {
        'websites': Website.objects.all(),
        'tags': Posts.tags.all(),
        'recent_posts': cache.get('fav_posts'),
    }
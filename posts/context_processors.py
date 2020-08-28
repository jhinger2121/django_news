from .models import Posts, Website

def get_websites_name(request):
    return {
        'websites': Website.objects.all()
    }
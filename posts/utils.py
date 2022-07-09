from .models import Posts, Website


def save_to_db(url, posts):
    if posts is None:
        print("there is no data to save")
        return
    for a_post in posts:
        if str(a_post['link']) != '' and str(a_post['title']) != '':
            website = 'Unknown'
            if 'djangostars' in url:
                website = 'DjangoStars'

            elif 'djangotricks' in url:
                website = 'DjangoTricks'

            elif 'djangoproject' in url:
                website = 'DjangoProject'
                if 'bugfix' in a_post['title']:  # adding tags based on title
                    a_post['tags'] = ['django', 'bugfix']
                elif 'DjangoCon' in a_post['title']:
                    a_post['tags'] = ['djangocon', 'django']
                else:
                    a_post['tags'] = ['django']
            elif 'number1' in url:
                website = 'NumberOne'
            elif 'justdjango' in url:
                website = 'JustDjango'
            elif 'djangocentral' in url:
                website = 'DjangoCentral'

            website = Website.objects.get_or_create(name=website)[0]
            post = Posts.objects.get_or_create(website=website, link=a_post['link'])[0]
            post.title = a_post['title']
            post.author = a_post['post_by']
            if post.created_at:
                pass
            else:
                post.created_at = a_post['created_at']
            post.rating = a_post['rating']
            post.comments = a_post['comments']
            post.visits = a_post['visits']
            for tag in a_post['tags']:
                post.tags.add(tag)
            post.save()
        else:
            print("Post does not contain url or title")
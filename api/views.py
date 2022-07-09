from posts.models import Posts
from api.serializers import PostsSerializer
from rest_framework import viewsets


class PostsViewsSets(viewsets.ModelViewSet):
    queryset =Posts.objects.all()
    serializer_class = PostsSerializer
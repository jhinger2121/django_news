from dataclasses import field
import imp
from posts.models import Posts, Website
from rest_framework import serializers


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):
    website = WebsiteSerializer()
    class Meta:
        model = Posts
        fields = ['url', 'id', 'title', 'link', 'website', 'headline', 'author', 'created_at', 'rating', 'comments', 'visits']
        # extra_kwargs = {
        #     'url': {'view_name': 'website', 'lookup_field': 'website'},
        #     'website' : {'lookup_field': 'name'}
        # }

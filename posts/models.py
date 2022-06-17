from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from taggit.managers import TaggableManager
from datetime import datetime, timedelta

class PostsQueryset(models.QuerySet):
    def get_number1_posts(self):
        return self.filter(website='number1')
    
    def get_djangostars_posts(self):
        return self.filter(website='djangostars')

    def get_djangotricks_posts(self):
        return self.filter(website='djangotricks')

    def get_djangoproject_posts(self):
        return self.filter(website='DjangoProject')

class PostsManager(models.Manager):
    def get_queryset(self):
        return PostsQueryset(self.model, using=self._db)
    
    def get_number1_posts(self):
        return self.get_queryset().get_number1_posts()

    def get_djangostars_posts(self):
        return self.get_queryset().get_djangostars_posts()
    
    def get_djangotricks_posts(self):
        return self.get_queryset().get_djangotricks_posts()

    def get_djangoproject_posts(self):
        return self.get_queryset().self.get_djangoproject_posts()

class Website(models.Model):
    name = models.CharField(_('Website'), max_length=50)

    class Meta:
        verbose_name = "Website"
        verbose_name_plural = "Websites"

    def __str__(self):
        return self.name

    def last_week_posts(self):
        now = datetime.now()
        seven_day_latter = now - timedelta(days=7)
        return self.posts_set.all()


class Posts(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=1000)
    link = models.URLField(_('Link'), max_length=1000)
    headline = models.TextField(_('Headline'))
    favourit = models.BooleanField(_('Favorit'), default=False)
    read_latter = models.BooleanField(_('Read Latter'), default=False)
    author = models.CharField(_('Author'), max_length=50, blank=True)
    created_at = models.DateTimeField(_('Created at'), null=True, blank=True)
    rating = models.IntegerField(_('Rating'), blank=True, null=True)
    comments = models.PositiveIntegerField(_('Comments'), blank=True, null=True)
    visits = models.PositiveIntegerField(_('Visits'), blank=True, null=True)
    
    tags = TaggableManager()
    objects = PostsManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

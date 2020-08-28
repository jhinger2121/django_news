from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('favourit/posts/', views.favourit_posts, name='favourit_posts'),
    path('favourit/add/<int:post_id>/', views.favourit_it, name='favourit_it'),
    path('read_latter/posts/', views.read_latter_posts, name='read_latter_posts'),
    path('tag=<str:tag>/', views.homepage, name="homepage"),
    path('<str:site_name>/', views.sort_by_site_name, name="sort_by_site_name"),
]
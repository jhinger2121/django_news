from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('tag=<str:tag_name>/', views.homepage, name="homepage"),
    path('about-me/', views.about, name="about_me"),

    path('post=<post_id>/', views.page_detail, name="page_detail"),

    path('<str:website_name>/', views.sort_by_website, name="sort_by_website"),
    path('<str:website_name>/&tag=<str:tag_name>/', views.sort_by_website, name="sort_by_website"),

    path('favourit/posts/', views.favourit_posts, name='favourit_posts'),
    path('favourit/add/<int:post_id>/', views.favourit_it, name='favourit_it'),
    path('read_latter/posts/', views.read_latter_posts, name='read_latter_posts'),
]
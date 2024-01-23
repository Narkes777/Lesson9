from .views import post_detail, get_published_posts, author_get_form
from django.urls import path, include

urlpatterns = [
    path('<int:pk>/', post_detail, name='post_detail'),
    path('posts/', get_published_posts, name='published_posts'),
    # path('posts/create', post_get_form, name='post_get_form'),
    # path('posts/create/save', post_post_form, name='post__form'),
    path('author/create', author_get_form, name='author_get_form'),
]


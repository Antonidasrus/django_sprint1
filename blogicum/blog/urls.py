from django.urls import path

import blog.views

app_name = 'blog'

urlpatterns = [
    path('', blog.views.index, name='index'),
    path('posts/<int:id>/', blog.views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', blog.views.category_posts,
         name='category_posts'),
]

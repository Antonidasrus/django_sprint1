from django.urls import path

import pages.views

app_name = 'pages'

urlpatterns = [
    path('about/', pages.views.About.as_view(), name='about'),
    path('rules/', pages.views.Rules.as_view(), name='rules'),
]

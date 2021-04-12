# this imports the views from this directory (the blog app)
from django.urls import path
from . import views

app_name = 'blog'   # This is here to keep things more organized and to use this name in the url in a template

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]

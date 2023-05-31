"""Defines URL patterns for blog Posts"""

from django.urls import path
from . import views

app_name = 'blog_posts'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all categories
    path('categories/', views.categories, name='categories'),
    # page 
]

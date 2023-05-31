from django.shortcuts import render
from .models import Category

def index(request):
    """The home page for the app"""
    return render(request, 'blog_posts/index.html')

def categories(request):
    """Show all categories"""
    categories = Category.objects.order_by('name')
    context = {'categories': categories}
    return render(request, 'blog_posts/categories.html', context)


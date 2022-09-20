from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Post
from .utils import update_views

# Create your views here.

# from django.http import HttpResponse


def home(request):
    forums = Category.objects.all()
    for forum in forums:
        forum.post_count = Post.objects.filter(categories=forum.id).count()

    context = {
        "forums": forums,
    }
    return render(request, 'home.html', context)


def rooms(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post": post
    }
    update_views(request, post)
    return render(request, 'rooms.html', context,)


def category(request, category_id):
    category = get_object_or_404(Category, slug=category_id)
    # posts = Post.objects.filter(approved=True, categories=category)
    posts = category.posts.filter(approved=True)

    context = {
        "posts": posts,
    }

    return render(request, 'threads.html', context)

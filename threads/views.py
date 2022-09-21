from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Post, Comment, Reply
from .utils import update_views
from .forms import PostForm
from django.contrib.auth.decorators import login_required

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
        "forums": category,
    }

    return render(request, 'threads.html', context)

@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            return redirect("home")
    context.update({
        "form": form,
        "title": "Create New Post"
    })
    return render(request, "register/create_post.html", context)

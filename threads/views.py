from django.shortcuts import render
# from .models import Author, Category, Post
from .utils import update_views

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request, 'home.html',)


def rooms(request):
    
    update_views(request, object)

    return render(request, 'rooms.html',)


def threads(request):
    return render(request, 'threads.html',)

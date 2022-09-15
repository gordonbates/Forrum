from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request, 'home.html',)


def rooms(request):
    return render(request, 'rooms.html',)


def threads(request):
    return render(request, 'threads.html',)

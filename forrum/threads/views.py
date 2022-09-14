from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    context = {
        'test': 'Hello',
        'posts': [1, 2, 3]
    }
    return render(request, 'home.html', context)

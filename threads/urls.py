from django.urls import path

from threads.views import home, rooms, threads

urlpatterns = [
    path('', home, name='home'),
    path('rooms/', rooms, name='rooms'),
    path('threads/', threads, name='threads'),
]

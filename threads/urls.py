from django.urls import path, include
from threads.views import home, rooms, category, create_post

urlpatterns = [
    path('', home, name='home'),
    path('rooms/<slug>', rooms, name='rooms'),
    path('category/<category_id>', category, name='category'),
    path('create_post', create_post, name='create_post'),
]

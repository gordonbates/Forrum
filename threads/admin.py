from django.contrib import admin
from .models import Category, Author, Post

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)

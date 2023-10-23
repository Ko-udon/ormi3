from django.contrib import admin
from .models import Post, Movie, BookInfo

admin.site.register(Post)
admin.site.register(Movie)
admin.site.register(BookInfo)
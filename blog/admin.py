from django.contrib import admin

# Register your models here.
from .models import Blog, BlogAuthor

admin.site.register(BlogAuthor)
admin.site.register(Blog)

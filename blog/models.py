from django.db import models

# Create your models here.
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

class BlogAuthor(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField()

    def get_abosulote_url(self):
        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    post_date = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

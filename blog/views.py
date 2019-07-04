from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Blog, BlogAuthor

def index(request):
    return render(request, 'index.html')

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

class BloggerListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 5

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('blog/', views.index, name='index'),
    path('', views.home, name='home'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogger/<int:pk>', views.BlogListbyAuthorView.as_view(), name='blogs-by-author'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blog/<int:pk>/comment/', views.BlogCommentCreate.as_view(), name='blog_comment'),
    path('blog/create', views.BlogCreate.as_view(), name='blog_create'),
]

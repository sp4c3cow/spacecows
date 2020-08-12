from django.urls import path
from django.conf.urls import include, url
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    #Blog section
    path("", PostListView.as_view(), name='blog-home'),
    path("user/<str:username>", UserPostListView.as_view(), name='user-posts'),
    path('post/<slug:slug>/', views.post_detail, name='post-detail'),
    path("posts/new/", PostCreateView.as_view(), name='post-create'),
    path("post/<slug:slug>/update/", PostUpdateView.as_view(), name='post-update'),
    path("post/<slug:slug>/delete/", PostDeleteView.as_view(), name='post-delete'),
    path("about/", views.about, name="blog-about"),
    path("<category>/", views.blog_category, name="blog_category"),
]

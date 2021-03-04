from django.urls import path
from . import views


app_name = 'posts'


urlpatterns = [
    path('', views.posts, name="home"),
    path('write/', views.CreatePosts.as_view(), name="posts_write"),
    path('politics/', views.posts_politics, name="politics"),
    path('economy/', views.posts_economy, name="economy"),
    path('it/', views.posts_it, name="it"),
    path('company/', views.posts_company, name="company"),
    path('society/', views.posts_science, name="science"),
    path('society/', views.posts_society, name="society"),
    path('book_review/', views.posts_bookreview, name="book_review"),
    path('<int:pk>/', views.PostDetail.as_view(), name="posts_detail"),
    path('edit/<int:pk>/', views.post_edit, name="posts_edit"),
    path('delete/<int:pk>', views.post_delete, name="posts_delete"),
]

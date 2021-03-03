from django.urls import path
from . import views


app_name = 'posts'


urlpatterns = [
    path('', views.posts, name="home"),
    path('write/', views.CreatePosts.as_view(), name="posts_write"),
    path('politics/', views.posts_politics, name="politics"),
    path('<int:pk>/', views.PostDetail.as_view(), name="posts_detail"),
    path('edit/<int:pk>/', views.post_edit, name="posts_edit"),
    path('delete/<int:pk>', views.post_delete, name="posts_delete"),
]

from django.urls import path
from . import views


app_name = 'posts'


urlpatterns = [
    path('', views.posts, name="home"),
    path('write/', views.post_write, name="posts_write"),
    path('<int:pk>/', views.PostDetail.as_view(), name="posts_detail")
]

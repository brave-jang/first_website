from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.log_out, name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup')
]
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserLoginForm

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(authentication_form=UserLoginForm),
        name='login'
    ),
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('images/', views.image_list, name='image_list'),
    path('users/', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<username>/', views.user_detail, name='user_detail'),
    path('people/', views.user_list, name='people_list'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]

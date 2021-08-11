from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register,name='register'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('user_logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="user_logout")
]
   
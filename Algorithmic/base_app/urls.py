from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_site, name='welcome'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_site, name='welcome'),
    path('register/', views.register, name='register'),
]


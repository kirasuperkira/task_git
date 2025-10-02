from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('posts/', views.post_list_view, name='post_list'),
]
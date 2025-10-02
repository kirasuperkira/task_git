from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home_view(request):
    return HttpResponse("<h1>Добро пожаловать в мой блог!</h1>")

def post_list_view(request):
    posts = Post.objects.all()
    html = "<h1>Все посты</h1><ul>"
    for post in posts:
        html += f"<li><strong>{post.title}</strong>: {post.content[:50]}...</li>"
    html += "</ul>"
    return HttpResponse(html)
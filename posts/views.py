from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Добро пожаловать в мой блог!</h1>")

def about_view(request):
    return HttpResponse("<h1>Вторая страница</h1>")
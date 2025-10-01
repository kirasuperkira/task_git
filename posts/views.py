from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Добро пожаловать в мой блог!</h1>")
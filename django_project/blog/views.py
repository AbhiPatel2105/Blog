from django.shortcuts import render
from .models import Posts


def home(request):
    context = {
        "posts": Posts.objects.all(),
        "title": "This is title given by you."
    }
    return render(request, 'blog/home.html', context = context)


def about(request):
    return render(request, 'blog/about.html')
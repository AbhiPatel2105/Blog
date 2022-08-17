from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

posts = [
    {
        "author": "abc",
        "title": "about django",
        "content": "this is post all about django.",
        "date_posted": "16 August 2022"
    },
    {
        "author": "xuz",
        "title": "about python",
        "content": "this is post all about python.",
        "date_posted": "17 August 2022"
    }
]

def home(request):
    context = {
        "posts": posts,
        "title": "This is title given by you."
    }
    return render(request, 'blog/home.html', context = context)


def about(request):
    return render(request, 'blog/about.html')
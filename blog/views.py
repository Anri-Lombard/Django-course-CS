from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),  # directly from database
    }
    return render(request, 'blog/home.html', context)  # template path


def about(request):
    return render(request, 'blog/about.html')

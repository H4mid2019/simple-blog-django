from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.all()
    return render(request, 'article.html', {'post': post, 'posts': posts})

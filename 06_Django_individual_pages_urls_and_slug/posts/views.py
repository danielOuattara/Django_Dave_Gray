from django.shortcuts import render
from .models import Post
# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', context={'posts': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/single-post.html', context={'post': post})

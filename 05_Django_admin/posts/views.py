from django.shortcuts import render
from .models import Post
# Create your views here.


def posts_list(request):
    """ list all posts """
    posts = Post.objects.all().order_by('-date')
    return render(
        request,
        template_name='posts/posts_list.html',
        context={'posts': posts}
    )

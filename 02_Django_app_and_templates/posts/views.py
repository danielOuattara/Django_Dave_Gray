from django.shortcuts import render

# Create your views here.


def posts_list(request):
    """Simple posts controller which always return a template on request """
    return render(request, 'posts/posts_list.html')

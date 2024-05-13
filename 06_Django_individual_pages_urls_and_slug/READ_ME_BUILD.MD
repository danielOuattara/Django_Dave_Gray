# 06 Django individual page, urls and slug

## (00:29)Getting Started

- start the virtual env: `source env/bin/activate`  then `cd 06_Django_individual_pages_urls_and_slug/`

## (01:04) Adding Post Slugs

- run the server: `python3 manage.py runserver`
- update the url bar to `http://localhost:8000/admin/` to login as admin.
- then login: enter username and password if necessary
- check every post entry has a `slug`

## (03:02) Applying a Named URL

- keep the server running
- go to: `06_Django_individual_pages_urls_and_slug/posts/urls.py`
- add a name `posts` to the `post` url as follow:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name="posts"),
]
```

- then go to : `06_Django_individual_pages_urls_and_slug/templates/layout.html`

- update the `nav` as follow to be able to use the name `posts` defined for posts in the urls.py module:

```html
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="{% url 'posts' %}">News</a> |
    </nav>
```

- go to browser and test the update
- the goal is to be able to easily create individual url to navigate to single post

## (05:44) Django Path Converters

- go to Django docs: `https://docs.djangoproject.com/en/5.0/topics/http/urls/#path-converters`

## (06:53) Applying a Slug Path Converter

- go back to `06_Django_individual_pages_urls_and_slug/posts/urls.py`
- update as follow:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name="posts"),
    path('<slug:slug>', views.post_page, name="single-post"),
]
```

where the first `slug` designates the dynamic parameter, and the second `slug` designates its actual value.

- then you need to create the controller `views.post_page` in `06_Django_individual_pages_urls_and_slug/posts/urls.py`

## (08:26) Create a post page view function

- go to `06_Django_individual_pages_urls_and_slug/posts/urls.py`
- create the new controller: `views.post_page`
- to do so update it as follow (for now) to get the echoed slug:

```py
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request, slug):
    return HttpResponse(slug)
```

## (09:27) Passing a parameter with a Named URL

- update `06_Django_individual_pages_urls_and_slug/posts/templates/posts/posts_list.html` as follow

```html
      <article class="post">
        <a href={% url 'single-post' slug=post.slug %}>
          <h2>{{post.title}}</h2>
        </a>
        <p>{{post.date}}</p>
        <p>{{post.body}}</p>
      </article>
```

- visit each post page to confirm that the slug is echoed back

## (11:59) Namespacing Named URLs

- create a Namespace for this Django app called `app_name = "posts"`
- to do so, update `06_Django_individual_pages_urls_and_slug/posts/urls.py` as follow:

```py
from django.urls import path
from . import views

app_name = "posts" #<-- Namespace

urlpatterns = [
    path('', views.posts_list, name="posts-list"),
    path('<slug:slug>', views.post_page, name="single-post"),
]

# Note: paths name have been updated !
```

- update `06_Django_individual_pages_urls_and_slug/templates/layout.html` accordingly to the new Namespace defined :

```html
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="{% url 'posts:posts-list' %}">News</a> |
    </nav>
```

- also update `06_Django_individual_pages_urls_and_slug/posts/templates/posts/posts_list.html` as follow, accordingly to the new Namespace defined :

```html
      <article class="post">
        <a href={% url 'posts:single-post' slug=post.slug %}>
          <h2>{{post.title}}</h2>
        </a>
        <p>{{post.date}}</p>
        <p>{{post.body}}</p>
      </article>
```

## (14:24) Updating the post page view function

- update controller in `06_Django_individual_pages_urls_and_slug/posts/views.py` to build a complete response for single post, not just an echoed slug response

```py
from django.shortcuts import render
from .models import Post
# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/single-post.html', {'post': post})

```

## (16:03) Creating a post page template

- create `single-post.html` template page as follow:

```html
{% extends 'layout.html'%}

{% block title%}
  {{post.title}} 
{% endblock %}


{% block content%}
<section>
  <h1> {{post.title}}</h1>
  <article class="post">
   <p>{{post.date}}</p>
   <p>{{post.body}}</p>
  </article>
  <a href={% url 'posts:posts-list' %}>
    <p>Back to all posts</p>
  </a>
</section>
  {% endblock %}



```

## (19:09) Bonus: Emoji Accessibility

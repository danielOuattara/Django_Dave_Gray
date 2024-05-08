# 05 Django Admin

## Getting Started

- start the virtual env: `source env/bin/activate`  then `cd 05_Django_admin/ &&`

## Finding the Django Admin

- the `Django Admin` feature provides tools that we would have to built ourself
- go `05_Django_admin/my_project/urls.py` and locate it:

```py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), # <-- HERE
    path('', views.homePage),
    path('about/', views.aboutPage),
    path('posts/', include('posts.urls')),
]

```

- run the server: `python3 manage.py runserver`
- navigate to `http://127.0.0.1:8000/admin`

## Creating a Super User

- stop the server: `ctrl + c`
- run `python3 manage.py createsuperuser`

```py
(env) daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Dave_Gray/05_Django_admin$ python3 manage.py  createsuperuser
Username (leave blank to use 'daniel'): 
Email address: daniel.ouattara@gmx.com
Password: 
Password (again): 
Superuser created successfully.
(env) daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Dave_Gray/05_Django_admin$ 
```

- start the server again: `python3 manage.py runserver`
- then login as admin at `http://127.0.0.1:8000/admin/login/admin/`

## Exploring the Admin Panel

- after login start exploring the admin panel
- explore `Groups` and `Users`

## Adding Content to the Admin Panel

- you can use this admin panel as a CMS
- got to `05_Django_admin/posts/admin.py`
- update as follow:

```py
from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)

```

- then navigate to `http://127.0.0.1:8000/admin/auth/user/` and confirm that `POSTS` has been added
- click on `Posts` in the `POSTS` section and confirm that there is 2 items in it

## Updating and Adding Posts to the Database

- click on any post item to see its content
- type text for each item in the panel, if you omit one item you won't be able to save the post
- save the updated post
- create a new post: click on `Add+` at the right of `Posts` label
- fill the fields for `Title` , `Body` and `Slug` the `Save`

## Displaying Posts with Template Tags

- back to editor to display these posts.
- go to `05_Django_admin/posts/views.py` and update its content as follow:

```py
from django.shortcuts import render
from .models import Post
# Create your views here.


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})
```

- there we import `Post` model from `models.py`
- and after retrieved `posts` from `Post`, we injected them as a Python dictionary, at 3rd parameters position in the `render` function

- go to  `05_Django_admin/posts/templates/posts/posts_list.html` and update it as follow:

```html
{% extends 'layout.html'%}

{% block title%}
  Posts 
{% endblock %}


{% block content%}
<section>
  <h1> Posts List</h1>
  <ul>

    {% for post in posts  %}
    <li>
      <article class="post">
        <h2>{{post.title}}</h2>
        <p>{{post.date}}</p>
        <p>{{post.body}}</p>
      </article>

    </li>
    {% endfor %}
  </ul>
</section>
  {% endblock %}

```

- you can order the post list by date descending, go to `05_Django_admin/posts/views.py` and update the module as follow

```py
from django.shortcuts import render
from .models import Post
# Create your views here.


def posts_list(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'posts/posts_list.html', {'posts': posts})
```

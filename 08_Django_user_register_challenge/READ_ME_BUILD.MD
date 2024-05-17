# Django User Register Challenge

## (00:25) The Challenge : Todo

- add a new app called `user`
- allow to navigate to `localhost:8000/user/register/`
- and display a heading there

## (01:47) The Solution: Getting Started

## (02:15) Create the users app

- create `user` app: `python3 manage.py startapp users`

## (02:49) Add users to installed apps

- go to `/my_project/settings.py`
- register `users` under `INSTALLED_APPS`

## (03:20) Add urls.py to users app

- go to `users/` app directory and create `urls.py`
 module

- then add content to  `users/urls.py` as follow:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
]
```

## (04:48) Update project urlpatterns

- upddate `my_project/urls.py` as follow:

```py
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('about/', views.aboutPage),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')), # <-- NEW !
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

## (05:45) Create the register view

- go to `users/views.py` and add `register controller` as follow:

```py
from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request, 'users/register.html')
```

## (06:42) Create the register template

- create `users/templates/users/register.html` as follow:

```html
{% extends 'layout.html' %}

{% block title %}

User

{% endblock %}

{% block content %}

<h1>Register User</h1>

{% endblock %}
```

## (08:26) A final quick change

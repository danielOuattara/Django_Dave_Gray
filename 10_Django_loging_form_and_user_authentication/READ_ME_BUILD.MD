# Django Login Form and User Authentication

## (00:27) Getting Started

- start the virtual env: `source env/bin/activate`  

- then  `cd 10_Django_loging_form_and_user_authentication/`

## (00:58) User Registration Page

- start the development server
  
```bash
python3 manager.py runserver 
```

## (01:40) Updating the Navbar

- update the Navbar to render a `Login page`

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
    <title>{% block title%} Django App {% endblock %}</title>
  </head>

  <body>
    <script src="{% static 'javascript/main.js'%}"></script>

    <nav>
      <a href="/" aria-label="home page">Home</a> |
      <a href="/about" aria-label="about page">About</a> |
      <a href="{% url 'posts:posts-list' %}" aria-label="news page">News</a> |
      <a href="{% url 'users:register' %}" aria-label="register">Register</a> |
      <a href="{% url 'users:login' %}" aria-label="login">Login</a>
    </nav>
    <main>{%block content%} {%endblock %}</main>
  </body>
</html>
```

## (03:25) Update the urlpatterns

- got to `/users/urls.py` and update the code as follow to add
  the `login` path

```py
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
]
```

## (04:41) Login View Function Part 1

- go to `/users/views.py` and create the `login` function

```py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


def register(request):
  ...


def login(request):
    if request.method == "POST":
        pass
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {"form": form})
```
  
## (07:28) Login Form Template

- go to  `/users/templates/users`

- create the login template: `login.html`

```html
{% extends 'layout.html' %} 

{% block title %} Login User {% endblock %} 

{% block content %}
  <h1>Login User</h1>
  <form action="/users/login" method="POST" class="form-with-validation">
    {% csrf_token %} {{ form }}
    <button class="form-submit">Submit</button>
  </form>
{% endblock %}
```

- navigate to `127.0.0.1:8000/users/login` and confirm its effective rendering

## (08:59) Login View Function Part 2

- go to `/users/views.py` to update the `login` function
  
```py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


def register(request):
  ...


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            # Logic For Login Here
            return redirect("posts:posts-list")
    else:
        form = AuthenticationForm(data=request.POST)
    return render(request, 'users/login.html', {"form": form})

```

## (11:05) Checking Form Logic & Validation

- go to the login page on the browser

- try to login with random credential and confirm login fail and that validation is provided  

- now use one of the two existing correct credentials to login successfully

## (12:32) Login View Function Part 3

- go back to `/users/views.py`

- import the `login` from `django.contrib.auth`

- then update the login:

```py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as _login
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # --> if only register user
            form.save()

            # --> if register & login at the same time
            # login(request,form.save())
            return redirect("posts:posts-list")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            _login(request, form.get_user())
            return redirect("posts:posts-list")
    else:
        form = AuthenticationForm(data=request.POST)
    return render(request, 'users/login.html', {"form": form})
```

## (14:24) Checking the Login Function

- navigate to `127.0.0.1:8000/users/login` and try to login
  as a none admin user

- confirm everything works

# Django User Register Completion

##  (00:27) Getting Started
  
- start the virtual env: `source env/bin/activate`  

- then  `cd 09_Django_user_registration/`

##  (00:55) Django's User Creation Form

- go to `users/views.py` views controllers

- import  built-in `UserCreationForm` class to allow create form

- create the `form`

- and pass it as a context through `render` function to `register.html` template

- update `register` as follow, until next recommendations:

```py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})
```

##  (03:09) Adding the form to a template

- go to `/users/templates/users/register.html`

- update it as follow, to be able to use the previously
  created form as context:

```html
{% extends 'layout.html' %}

{% block title %}

User

{% endblock %}

{% block content %}

<h1>Register User</h1>
<form action="/users/register" method="POST" class="form-with-validation">
    {{ form }}
    <button>Submit</button>
</form>

{% endblock %}
```

- do not forget to grab the CSS class definition from Dave's github page

##  (05:09) The CSRF Token

- security concern

- to avoid CSRF add `csrf_token` as follow in `register.html` template:

```html
{% extends 'layout.html' %}

{% block title %}

User

{% endblock %}

{% block content %}

<h1>Register User</h1>
<form action="/users/register" method="POST" class="form-with-validation">
    {% csrf_token %}
    {{ form }}
    <button>Submit</button>
</form>

{% endblock %}
```

##  (05:52) Checking the form in the browser

- do it in browser, navigate to `users/register` after starting the server

##  (07:48) Saving the User after form submission

- go to `users/views.py` controllers

- import `redirect` to redirect upon form submitted successfully

- update the `register` controller as follow:

```py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:posts-list")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})
```

##  (11:35) Checking form logic

- check effective user register

- check register failure: duplicate username, password, etc...

##  (13:16) Verifying the new user was saved

- navigate to `http://localhost:8000/admin`

- log as admin and verify the newly added user

##  (13:54) Update the Navbar

- update `/users/urls.py` as follow:

```py
from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path('register', views.register, name="register"),
]

```

- in `/templates/layout.html`, add a link to navigate to user registration

```html
<a href="{% url 'users:register' %}">Register</a>
```

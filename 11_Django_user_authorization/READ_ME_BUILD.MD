# Python Django User Authorization

##  (00:25) Getting Started

- start the virtual env: `source env/bin/activate`  

- then  `cd 11_Django_user_authorization/`

##  (00:53) Lesson Goals

- user `registration` and `login` processes have already
  been created in the previous parts

- in this part the goal is to provide with `authorization`

- also add a `logout` logic

##  (01:12) Adding a logout

- go to `/users/urls.py`

- add a logout path:

```py
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"), # <-- NEW !
]
```

- after that go to `/users/views.py`

- import `logout` from `django.contrib.auth` and create a `logout` function

```py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as _login, logout as _logout
# Create your views here.


def register(request):
  ...

def login(request):
  ...

def logout(request):
    if request.method == "POST":
        _logout(request)
        return redirect("posts:posts-list")
```

- go to `/static/css/styles.css`
  and add some CSS

```css
.logout{
  display: inline-block;
}

.logout-button {
  font-size: 2.5rem;
  background-color: rgb(0,0,0,0);
  border: none;
}

.logout-button:hover {
  opacity: 0.85;
}
```

- go to `/templates/layout.html`

- add a link to `logout`

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
    <!-- ... -->
      <form action="{%url 'users:logout' %}" method="POST" class="logout">
        {% csrf_token %}
        <button class="logout-button" aria-label="User Logout button" title="User Logout">Logout</button>
      </form>
    </nav>
    <main>{%block content%} {%endblock %}</main>
  </body>
</html>

```

- run the dev server and check the `logout action` is effective

##  (07:32) Adding a New Post page

- let's create a protected page, witch requires users to be logged
  in order to create a new post

- go to `/posts/urls.py` and update:
  
```py
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.posts_list, name="posts-list"),
    path('new-post', views.post_new, name="post-new"), # <--NEW !
    path('<slug:slug>', views.post_page, name="single-post"),
]
```

- now go to `/posts/views.py` and update:

```py
from django.shortcuts import render
from .models import Post
# Create your views here.


def posts_list(request):
    ...

def post_page(request, slug):
    ...

def post_new(request):
    return render(request, 'posts/new-post.hmtl')
```

- create `/posts/templates/posts/new-post.html`

```html
{% extends 'layout.html'%}

{% block title%}
 New post
{% endblock %}


{% block content%}
    <section>
        <h1>New post</h1>
    </section>
{% endblock %}
```

- go to root `/templates/layout.html` and add a link to render the new post page

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
      <a href="{% url 'posts:new-post' %}" aria-label="new post">New post</a> |
      <a href="{% url 'users:login' %}" aria-label="login">Login</a> |
      <form action="{%url 'users:logout' %}" method="POST" class="logout">
        {% csrf_token %}
        <button class="logout-button" aria-label="User Logout button" title="User Logout">Logout</button>
      </form>
    </nav>
    <main>{%block content%} {%endblock %}</main>
  </body>
</html>
```

##  (13:01) Applying User Authorization

- go to `/posts/views.py` and update the code so that only logged-in user can add a new post.

```py
from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required # <--NEW
# Create your views here.


def posts_list(request):
    ...


def post_page(request, slug):
    ...

@login_required(login_url="/users/login") # <-- NEW
def post_new(request):
    return render(request, 'posts/new-post.html')
```

- use the browser to check the logic is effective

##  (15:18) Using the "next" redirect value

- when a user is not logged in try to navigate to `New post`,
  the user is redirected to `/users/login` .
  
- The URL address looks like this:
`http://127.0.0.1:8000/users/login?next=/posts/new-post`

- The `?next=/posts/new-post` section indicates that upon successful
  login, the user will be redirected to `/posts/new-post`, where the
  user initially request to navigate to.

- Now according to a particular UI design architecture, we can have
  a control above that default behavior, to redirect a particular place

- go to `/users/templates/users/login.html` and update the code:
  
```html
{% extends 'layout.html' %} 

{% block title %} Login User {% endblock %} 

{% block content %}
  <h1>Login User</h1>
  <form action="/users/login" method="POST" class="form-with-validation">
    {% csrf_token %} 
    
    {{ form }}

<!-- NEW -->
    {% if request.GET.next %}
      <input type="hidden" name="next" value="{{ request.GET.next}}">
    {% endif %}
<!--  -->
    <button class="form-submit">Submit</button>
  </form>
{% endblock %}
```

- this will attach an hidden input, carrying a data in its value
  attribute that will be analyzed in the corresponding view (controller)

- now go to `/users/views.py`, and update the code for `login` to handle
  a possible `request.GET.next` value

```py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as _login, logout as _logout
# Create your views here.


def register(request):
    ...


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            _login(request, form.get_user())
            # NEW -----
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            # ---------
            else:
                return redirect("posts:posts-list")
    else:
        form = AuthenticationForm(data=request.POST)

    return render(request, 'users/login.html', {"form": form})


def logout(request):
    ...
```

- go to the browser and check it works

##  (20:12) Conditional Navbar Links

- show/not show some of the items in the navbar

- in template, we have access to user object

- go to `/templates/layout.html` and update the code to add condiditons

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

<!-- NEW -->
      {% if user.is_authenticated %}
        <a href="{% url 'posts:new-post' %}" aria-label="new post">New post</a> |
        <form action="{%url 'users:logout' %}" method="POST" class="logout">
          {% csrf_token %}
          <button class="logout-button" aria-label="User Logout button" title="User Logout">Logout</button>
        </form>

      {% else %}
        
        <a href="{% url 'users:register' %}" aria-label="register">Register</a> |
        <a href="{% url 'users:login' %}" aria-label="login">Login</a>
      {% endif %}
<!--  -->

      {% if user.is_authenticated %}
      {% endif %}
    </nav>
    <main>{%block content%} {%endblock %}</main>
  </body>
</html>
```

- go to browser and confirm effective

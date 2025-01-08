#  02 Django App & Templates

## start this section

- copy the folder 01_introduction to 02_Django_app_and_templates
  
- activate the virtual env

## add VS CODE extension

- install VS CODE Django extension `Django` by `Baptiste Darthernay`

## create a new django app

- create an new app: `python3 manage.py startapp posts`
  
- create a `view` at `/posts/views.py`:

    ```py
    from django.shortcuts import render

    # Create your views here.


    def posts_list(request):
        return render(request, '')
    ```

## Add the new app to the global Project

- connect the new app to the global project: add `posts` in the `INSTALLED_APPS` list at `/my_project/settings.py`

## Add templates

- `touch /posts/templates/posts/post_list.html`
  
- type `ctrl + ,` and search `emmet Include Language` to add `django-html` and `html` as value
  
- use emmet shortcut `!` in `post_list.html` to populate with basic html boilerplate

## App URLs

- `touch /posts/urls.py`
  
- add the following to the newly created `urls.py`

    ```py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.posts_list),
    ]
    ```

## Link Apps URLs to main project URLs

- update `/my_project/urls.py` as follow:

    ```py
    from django.contrib import admin
    from django.urls import path, include
    from . import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.homePage),
        path('about/', views.aboutPage),
        path('posts/', include('posts.urls')),
    ]
    ```

## Running the sever

- check the server running

- navigate to `http://127.0.0.1:8000/posts` and confirm running

- notice the styling is not updated

##  Adding CSS

- update the css style for `/static/css/styles.css`

## Create a base layout template

- `touch /templates/layout.html`
  
- add the following:

    ```html
    <!DOCTYPE html>
    {% load static %}
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
        <title>
            {% block title %}
            Django App
            {% endblock %}
        </title>
    </head>
    <body>

        <script src="{% static 'javascript/main.js'%}"></script>

        <nav>
            <a href="/">Home</a> |
            <a href="/about">About</a> |
            <a href="/posts">News</a> |
        </nav>
        <main>
            {%block content %}
            {%endblock %}
        </main>
        
    </body>
    </html>
    ```

## Extending the layout template

- update `/templates/index.html` as follow:

    ```html
    {% extends 'layout.html'%}

    {% block title%}
    Home
    {% endblock %}



    {% block content%}
    <h1>Home Page</h1>
    <p>Check out my <a href="/about"> about page</a></p>
    {% endblock %}
    ```

- update `/templates/about.html` as follow:

    ```html
    {% extends 'layout.html'%}

    {% block title%}
    Home
    {% endblock %}


    {% block content%}
        <h1>About Page</h1>
        <p>Back to <a href="/"> Home page</a></p>
    {% endblock %}
    ```

- `/posts/templates/posts/posts_list.html` a follow:

    ```html
    {% extends 'layout.html'%}

    {% block title%}
    Post list
    {% endblock %}


    {% block content%}
    <h1> Home Post list</h1>
    {% endblock %}
    ```

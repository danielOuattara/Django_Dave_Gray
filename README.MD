# 01 introduction

## Create a virtual environment

- create the project folder like `django_project`
- create a virtual environment: `python3 -m venv env`

##  Install Django

- install `Django` using `pip`
- check `Django` installed: `pip freeze`

## Create the a new Django project

- create a django project: `django-admin startproject my_project`

## Start server

- `cd my_project` directory
- `python3 manage.py runserver`.

## Creating basic Views for homePage and aboutPAge

- create `views.py` in the root of the project

- add the following :

```python
    from django.http import HttpResponse

    def homePage(request):
        return HttpResponse("Hello Django World! ")

    def aboutPage(request):
        return HttpResponse("About Page")
```

- test browser navigation on `/` and `about`
- cd one level up
- `mkdir templates` in the same level that `my_project/`
- create `index.html` and add the following content:

```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
    </head>
    <body>
        <h1>Home Page</h1>
        <p>Check out my <a href="/about"> about page</a></p>
    </body>
    </html>

```

- create `about.html` and add the following content:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>About Page</h1>
    <p>Back to <a href="/"> Home page</a></p>
  </body>
</html>
```

##  URLs and Views

- in the `my_projects/settings.py` add the following in the `TEMPLATES --> DIRS` list : `'DIRS': ['templates'],`

##  Adding HTML templates

- update `my_project/views/py` as follow:

```python
# from django.http import HttpResponse

from django.shortcuts import render


def homePage(request):
    # return HttpResponse("Hello Django World! ")
    return render(request, 'index.html')


def aboutPage(request):
    # return HttpResponse("About Page")
    return render(request, 'about.html')
```

## Static CSS Link

- create `static/` folder in the same level as `templates/` folder
- create `static/css/styles.css` file
- add the following style defintions to the `styles.css` :

```css
* {
margin: 0;
padding: 0;
box-sizing: border-box;

}

body {
min-height: 100vh;
display: grid;
place-content: center;
font-size: 2rem;
background-color: rgb(39, 39, 39);
color: whitesmoke;
}

h1,
p {
text-align: center;
}

h1 {
color: rgb(34, 34, 207);
}

```

- in `my_project/settings.py` do the following:
  - `import os` on the top
  - add

    ```python
        STATIC_URL = 'static/'
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'static')
        ]
    ```

- update `templates/index.html` as follow:

 ```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Home</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  </head>
  <body>
    <h1>Home Page</h1>
    <p>Check out my <a href="/about"> about page</a></p>
  </body>
</html>
```

- update `templates/about.html` as follow:

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>About</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  </head>
  <body>
    <h1>About Page</h1>
    <p>Back to <a href="/"> Home page</a></p>
  </body>
</html>

```

## Javascript script

- create `templates/javascript/main.js` and add `console.log("This is from your about page");`

- update `templates/about.html` as follow:

```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>About</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  </head>
  <body>
    <h1>About Page</h1>
    <p>Back to <a href="/"> Home page</a></p>
    <script src="{% static 'javascript/main.js'%}"></script>
  </body>
</html>

```

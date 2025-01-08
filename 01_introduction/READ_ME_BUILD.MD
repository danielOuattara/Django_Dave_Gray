# 01 introduction

## Create a virtual environment

- create the project folder like `django_project`
  
- create a virtual environment:

```bash
  python3 -m venv env
```

- activate the new virtual environment created:

```bash
  source env/bin/activate`
```

##  Install Django

- install `Django` using `pip3`

```bash
  python3 -m pip3 install Django
```

- check `Django` installed: ``
  
```sh
pip3 freeze

# or

python3 -m django --version

# or

django-admin --version
```

## Create the a new Django project

- create a django project: `django-admin startproject my_project`

## Start server

- `cd my_project/` directory

- run the development server : `python3 manage.py runserver`

- navigate to `http://127.0.0.1:8000` to check application server running
  
## URLs and Views

- update `/my_project/urls.py` as follow:

  ```py
    from django.contrib import admin
    from django.urls import path
    from . import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.homePage),
        path('about/', views.aboutPage),
    ]
  ```

## Creating basic Views for homePage and aboutPage

- create `/my_project/views.py` in the root of the project

- add the following to it:

  ```python
      from django.http import HttpResponse

      def homePage(request):
          return HttpResponse("Hello Django World! ")

      def aboutPage(request):
          return HttpResponse("About Page")
  ```

- test browser: navigate to
  - `http://127.0.0.1:8000/` and
  - `http://127.0.0.1:8000/about/`

## Adding HTML Templates

- cd one level up
  
- `mkdir templates` in the same level that `my_project/`
  
- `touch ./templates/index.html` and add the following content:

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Home</title>
  </head>
  <body>
      <h1>Home Page</h1>
      <p>Check out my <a href="/about"> about page</a></p>
  </body>
  </html>
  ```

- `touch ./templates/about.html` and add the following content:

  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>About</title>
    </head>
    <body>
      <h1>About Page</h1>
      <p>Back to <a href="/"> Home page</a></p>
    </body>
  </html>
  ```

- in the `my_projects/settings.py` add `templates/` in the `TEMPLATES` list as follow:

  ```py
  TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # <---
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
  ]
  ```

## Adding HTML templates

- update `my_project/views.py` as follow:

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

- test browser: navigate to
  - `http://127.0.0.1:8000/` and
  - `http://127.0.0.1:8000/about/`
  
## Static CSS Link

- create `static/` folder in the same level as `templates/` folder

- `touch static/css/styles.css` file

- add the following style definition to the `styles.css` :

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

- in `my_project/settings.py` do the following to make `static/` folder visible by Django:
  - `import os` on the top
  
  - add :

  ```python
  STATIC_URL = 'static/'

  STATICFILES_DIRS = [
      os.path.join(BASE_DIR, 'static'),
  ]
  ```

- update `/templates/index.html` as follow:

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

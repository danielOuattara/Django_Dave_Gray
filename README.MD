# Process

- create a folder like `django_project`
- create a virtual environment: `python3 -m venv env`
- install `Django` using `pip`
- create `Django` installed: `pip freeze`
- create a django project: `django-admin startproject my_project`
- `cd my_project` directory
- `python3 manage.py runserver`. The server should run by default on port `localhost:8000`
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

- in the `my_projects/settings.py` add the following in the `TEMPLATES -> DIRS` list : `'DIRS': ['templates'],`

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

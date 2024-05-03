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

# 03 Django Models and Migrations

## Getting Started

- start the virtual env: `source env/bin/activate` then `cd 03_Django_models_and_migrations/`

## What are Django Models?

## Creating a Model

- `cd 03_Django_models_and_migrations/posts/models.py`
- create/define a model for `post` as follow:

  ```py
  from django.db import models

  # Create your models here.

  class Post(models.Model):
      title = models.CharField(max_length=75)
      body = models.TextField()
      slug = models.SlugField()
      date = models.DateTimeField(auto_now_add=True)
  ```

## Create and Apply Migrations

- start the server: `python3 manage.py runserver`
  
- check again that Django warns us about `unapplied migrations ...`
  
- on creating the project `Django` comes with internal models and
  migrations that are not applied yet
  
- run `python3 manage.py migrate` to apply all the migrations
  
- that command run the Django internal migrations, but not ours
  
- so first, let's make/create our migrations by running
  `python3 manage.py makemigrations`

  ```bash
  (env) daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Dave_Gray/03_Django_models_and_migrations$ python3 manage.py makemigrations
  Migrations for 'posts':
    posts/migrations/0001_initial.py
      - Create model Post
  (env) daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Dave_Gray/03_Django_models_and_migrations$ 
  ```

- run `python3 manage.py migrate` to apply our migrations

  ```bash
  (env) daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Dave_Gray/03_Django_models_and_migrations$ python3 manage.py migrate
  Operations to perform:
    Apply all migrations: admin, auth, contenttypes, posts, sessions
  Running migrations:
    Applying posts.0001_initial... OK
  (env) daniel@debian-dbo:~/Documents/Computing/Python_DJANGO/Django_Dave_Gray/03_Django_models_and_migrations$ 
  ```

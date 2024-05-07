# 03 Django Models and Migrations

## Getting Started

- start the virtual env: `cd 04_Django_ORM_intro/ && source env/bin/activate`

## What is an ORM?

- ORM = Object Relational Mapper

## Django Interactive Console

- `python3  manage.py shell` to go to interactive shell

## Creating and Saving a Post in interactive console

 ```sh
  >>> from posts.models import Post
  >>> p = Post()
  >>> p.title = "My first post!"
  >>> p.save()
  >>> Post.objects.all()
  >>> exit()
  ```

## Adding a Method

- go to `04_Django_ORM_intro/posts/models.py`
- update as:

```py
from django.db import models

# Create your models here

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

```

## Saving a 2nd Post to the Database

- `python3  manage.py shell` to go to interactive shell

 ```sh
  >>> from posts.models import Post; p = Post() ; p.title = "My second post!"; p.save() ; Post.objects.all(); exit()
  ```

## Exiting the Shell

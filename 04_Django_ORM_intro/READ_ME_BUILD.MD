# 04 Django ORM Intro

## Getting Started

- start the virtual env: `source env/bin/activate` then `cd 04_Django_ORM_intro/`

## What is an ORM?

- ORM = Object Relational Mapper
  
- in this part we will explore the the Django ORM in Django Shell

## Django Interactive Console

- `python3 manage.py shell` to go to interactive shell

## Creating and Saving a Post in interactive console

  ```sh
    >>> from posts.models import Post
    >>> p = Post()
    >>> p 
    <Post: Post object (None)> # <-- Response : No post object saved in the database yet !
    >>> p.title = "My first post!"
    >>> p.save()
    >>> Post.objects.all()
    <QuerySet [<Post: Post object (1)>]> # <-- Response :  1 post object in the database
    >>> exit()
  ```

## Adding a Method

- go to `/posts/models.py`
  
- update as to simply add a new method in the model,
  so no migration needed

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
- type in those command to see what is in the

  ```sh
  >>> from posts.models import Post; p = Post() ; p.title = "My second post!"; p.save() ; Post.objects.all(); exit()
  ```

## Exiting the Shell

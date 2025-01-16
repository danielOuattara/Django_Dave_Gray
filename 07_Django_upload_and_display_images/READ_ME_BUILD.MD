#   07 Django Upload and Display Images

##  (00:26) Getting Started

- start the virtual env: `source env/bin/activate`  

- then  `cd 07_Django_upload_and_display_images/`

##  (01:00) Image Settings

- go to `/my_project/settings.py`

- navigate to under `STATICFILES_DIRS` list and add `MEDIA_URL`  and a `MEDIA_ROOT` as follow:

```py
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

##  (02:44) Updating URL Patterns

- go to `/my_project/urls.py`
  
- update as follow:

```py
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('about/', views.aboutPage),
    path('posts/', include('posts.urls')),
]

# tell the Django project where to find images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

##  (04:30) Adding a dependency

- install `Pillow`: run `pip3 install Pillow`

##  (05:24) Updating the Post Model

- go to `/posts/models.py`

- update the post model as follow:

```py
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title
```

- run a post model migration to take take its update:
  `python3 manage.py makemigrations`

- now apply those migrations: `python3 manage.py migrate`

##  (07:32) Adding Images to Posts

- run the server: `python3 manage.py runserver`

- got to admin panel: `http://127.0.0.1:8000/admin/`

- then login: provide username and password if any

- go `posts` and check that `Banner` is now present for any post item

- select browse to grab an image for each post

- let one post without image

##  (09:24) Adding the Fallback Image

- check in root that `media/` has been created

- add there a `fallback.png` image as a fallback image

##  (09:56) Displaying Images in Templates

- go to `posts/templates/posts/single-post.html`

- update the template as follow:

```py
{% extends 'layout.html'%}

{% block title%}
  {{post.title}} 
{% endblock %}


{% block content%}
<section>
  <img src="{{ posts.banner.url}}" alt="{{post.title}}" class="banner"/>
  <h1> {{post.title}}</h1>
  <article class="post">
   <p>{{post.date}}</p>
   <p>{{post.body}}</p>
  </article>
  <a href={% url 'posts:posts-list' %}>
    <p>Back to all posts</p>
  </a>
</section>
  {% endblock %}
```

- add some style: go to `/static/css/styles.css`

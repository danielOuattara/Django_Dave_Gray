from django.urls import path
from . import views

urlpatterns = [
    # path('', views.regi),
    path('register', views.register),
]

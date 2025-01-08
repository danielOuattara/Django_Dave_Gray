# from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    """Home page controller"""
    # return HttpResponse("Hello Django World! ")
    return render(request, 'index.html')


def about_page(request):
    """About page controller"""
    # return HttpResponse("About Page")
    return render(request, 'about.html')

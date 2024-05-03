# from django.http import HttpResponse

from django.shortcuts import render


def homePage(request):
    # return HttpResponse("Hello Django World! ")
    return render(request, 'index.html')


def aboutPage(request):
    # return HttpResponse("About Page")
    return render(request, 'about.html')

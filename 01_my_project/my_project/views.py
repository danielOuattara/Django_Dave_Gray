from django.http import HttpResponse


def homePage(request):
    return HttpResponse("Hello Django World! ")


def aboutPage(request):
    return HttpResponse("About Page")

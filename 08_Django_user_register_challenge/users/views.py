from django.shortcuts import render

# Create your views here.


def register(request):
    """User register controller"""
    return render(request, 'users/register.html')

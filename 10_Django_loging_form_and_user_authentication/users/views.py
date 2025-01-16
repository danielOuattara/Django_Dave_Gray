from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as _login
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # --> if only register user
            form.save()

            # --> if register & login at the same time
            # _login(request, form.save())
            return redirect("posts:posts-list")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            _login(request, form.get_user())
            return redirect("posts:posts-list")
    else:
        form = AuthenticationForm(data=request.POST)
    return render(request, 'users/login.html', {"form": form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import login
@login_required
def home(request):
    return render(request, 'newsfeed/home.html')


def root(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        return redirect('login')
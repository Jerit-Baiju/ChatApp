from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import redirect, render

from .models import User

# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
            context = {
                'navbar': False
            }
            return render(request, 'accounts/login.html', context)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            try:
                url = request.POST.get('next')
                cache.clear()
                return redirect(url)
            except:
                cache.clear()
                return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')
            context = {
                'navbar': False
            }
            return render(request, 'accounts/login.html', context)
    context = {
        'navbar': False
    }
    return render(request, 'accounts/login.html', context)


def register_page(request):
    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    cache.clear()
    return redirect('home')

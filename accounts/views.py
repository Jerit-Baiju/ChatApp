# from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import User

# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            return HttpResponse('User does not exist')
            # return render(request, 'login.html')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            try:
                url = request.POST.get('next')
                cache.clear()
                return redirect(url)
            except:
                cache.clear()
                return redirect('index')
        else:
            return HttpResponse( 'Username OR password does not exit')
    return render(request, 'login.html')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        name = request.POST['name'].lstrip().rstrip()
        email = request.POST['email']
        password = request.POST['password1']
        confirm = request.POST['password2']
        name_split = name.split(' ')
        if len(name_split) <= 1:
            return HttpResponse(request, 'Please enter your full name.')
        first_name = name.split()[0].capitalize()
        last_name = name.split()[1].capitalize()
        if password == confirm:
            if User.objects.filter(email=email).exists():
                return HttpResponse(request, 'Email already exists.')
            user = User.objects.create_user(
                email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            login(request, user)
            try:
                url = request.POST.get('next')
                cache.clear()
                return redirect(url)
            except:
                cache.clear()
                return redirect('index')
        else:
            return HttpResponse(request, 'Passwords does not match.')
    else:
        return render(request, 'register.html', {'title': 'Register | Jerit Baiju'})


def logout_page(request):
    logout(request)
    cache.clear()
    return redirect('home')

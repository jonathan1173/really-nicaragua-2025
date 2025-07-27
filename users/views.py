from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth import logout
from .models import Favorite
from django.http import JsonResponse
@never_cache
def page_register(request):
    if request.user.is_authenticated:
        return redirect('/home')
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('/home')
        else:
            print(form.errors)
            messages.error(request, "Por favor corrige los errores.")
    else:
        form = UserForm()

    return render(request, 'users/register.html', {'form': form})

@never_cache
def page_login(request):
    if request.user.is_authenticated:
        return redirect('/home')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, "Credenciales inválidas")

    return render(request, 'users/login.html')

@login_required(login_url='/users/login')
@never_cache
def view_profile(request):
    user = request.user
    favorites = Favorite.objects.filter(user=request.user)
    return render(request,'users/profile.html', {
        'user':user,
        'favorites': favorites
        })


def logout_view(request):
    logout(request)
    response = redirect('users-login')

    response.delete_cookie('some_cookie_name')

    return response



@login_required
def toggle_favorite(request):
    url = request.GET.get('url')
    title = request.GET.get('title', '')

    fav, created = Favorite.objects.get_or_create(user=request.user, url=url)

    if created:
        fav.title = title  
        fav.save()
        status = 'added'
    else:
        fav.delete()
        status = 'removed'

    return JsonResponse({'status': status})


@login_required
def is_favorite(request):
    url = request.GET.get('url')
    is_fav = Favorite.objects.filter(user=request.user, url=url).exists()
    return JsonResponse({'favorite': is_fav})

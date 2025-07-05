from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserForm

def page_register(request):
    if request.user.is_authenticated:
        return redirect('/home')
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            messages.success(request, "Registro exitoso. Has iniciado sesión.")
            return redirect('/home')
        else:
            messages.error(request, "Por favor corrige los errores.")
    else:
        form = UserForm()

    return render(request, 'users/register.html', {'form': form})


def page_login(request):
    if request.user.is_authenticated:
        return redirect('/home')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect('/home')
        else:
            messages.error(request, "Credenciales inválidas")

    return render(request, 'users/login.html')

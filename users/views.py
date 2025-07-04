from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm

def page_register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})


def page_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')  # ajustalo a tu vista principal
        return render(request, 'users/login.html', {"error": "Credenciales inválidas"})
    return render(request, 'users/login.html')

from django.shortcuts import render

def page_register(request):
    return render(request, 'users/register.html')

def page_login(request):
    return render(request, 'users/login.html')
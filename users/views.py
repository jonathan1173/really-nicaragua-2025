from django.shortcuts import render, redirect
from .forms import UserForm

def page_register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-login')
    else:
        form = UserForm()
    
    return render(request, 'users/register.html', {'form': form})

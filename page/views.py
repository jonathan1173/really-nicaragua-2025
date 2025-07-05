from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
def page_index(request):
    return render(request, 'rally_nicaragua/index/index.html')

@login_required(login_url='users-login')
@never_cache
def page_home(request):
    return render(request, 'page/home.html')
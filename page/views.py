from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import Department

def page_index(request):
    return render(request, 'rally_nicaragua/index/index.html')

@login_required(login_url='users-login')
@never_cache
def page_home(request):
    return render(request, 'page/home.html')

@login_required(login_url='users-login')
@never_cache
def page_maps(request):
    return render(request, 'page/maps.html')


@login_required(login_url='user-login')
@never_cache
def page_department(request, city):
    department = Department.objects.filter(name=city).first()
    municipalities = department.municipalities.all() if department else None

    return render(request, "page/municipality.html", {
        "department": department,
        "municipalities": municipalities,
    })
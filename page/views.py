from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import Department, Municipality, MunicipalityContent
from django.shortcuts import get_object_or_404

# renderiza la pagina de inicio
def page_index(request):
    return render(request, 'rally_nicaragua/index/index.html')

# renderiza la pagina home 
@login_required(login_url='users-login')
@never_cache
def page_home(request):
    return render(request, 'page/home.html')

# renderiza la pagina que contiene el mapa 
@login_required(login_url='users-login')
@never_cache
def page_maps(request):
    return render(request, 'page/maps.html')

# filtra en base al mapa 
@login_required(login_url='user-login')
@never_cache
def page_department(request, city):
    department = Department.objects.filter(name=city).first()
    municipalities = department.municipalities.all() if department else None

    return render(request, "page/municipality.html", {
        "department": department,
        "municipalities": municipalities,
    })

# selección de categoría
@login_required(login_url='user-login')
@never_cache
def municipality_options(request, municipality_name):
    municipality = get_object_or_404(Municipality, name=municipality_name)
    return render(request, "page/municipality_options.html", {
        "municipality": municipality,
    })

# muestra contenido de categoría
@login_required(login_url='user-login')
@never_cache
def municipality_content(request, municipality_name, category):
    municipality = get_object_or_404(Municipality, name=municipality_name)
    content = MunicipalityContent.objects.filter(municipality=municipality, category=category).first()
    return render(request, "page/municipality_content.html", {
        "municipality": municipality,
        "category": category,
        "content": content,
    })

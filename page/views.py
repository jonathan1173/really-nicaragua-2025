from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .models import Department, Municipality, Content, Category
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

# renderiza la pagina de inicio
def page_index(request):
    return render(request, 'rally_nicaragua/index.html')

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


@login_required(login_url='user-login')
@never_cache
def municipality_options_and_content(request, municipality_name):
    municipality = get_object_or_404(Municipality, name=municipality_name)
    department = municipality.department
    categories = Category.objects.all()

    category_name = request.GET.get('category')  
    content_html = ''
    selected_category = None

    if category_name:
        selected_category = get_object_or_404(Category, name=category_name)
        content = Content.objects.filter(municipality=municipality, category=selected_category).first()

        return JsonResponse({
            "category": selected_category.name,
            "municipality": municipality.name,
            "content": content.content if content else None
        })


    # Si no hay categoría, solo devuelve la página base con las categorías
    return render(request, "page/municipality_options.html", {
        "municipality": municipality,
        "department": department,
        "categories": categories,
    })

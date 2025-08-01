from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
# Se actualizan los modelos importados para reflejar la nueva estructura
from .models import Department, Municipality, Category, CategoryPage, ContentItem, Event
from django.db.models import Q

# renderiza la pagina de inicio
def page_index(request):
    return render(request, 'rally_nicaragua/index.html')

# renderiza la pagina home 
@login_required(login_url='/users/login')
@never_cache
def page_home(request):
    return render(request, 'page/home.html')

# renderiza la pagina que contiene el mapa 
def page_maps(request):
    departments = Department.objects.all()
    return render(request, 'page/maps.html', {'departments': departments})

# Muestra los municipios de un departamento y su infomacion
def page_department(request, department_slug):
    department = Department.objects.filter(slug=department_slug).first()

    if not department:
        return render(request, "page/department.html", {
            "error_message": "El departamento solicitado no está disponible.",
            "department": None,
            "municipalities": []
        })

    municipalities = department.municipalities.all()
    return render(request, "page/department.html", {
        "department": department,
        "municipalities": municipalities
    })

# Muestra el detalle de un municipio y las categorías de contenido que tiene disponibles.
def municipality_detail(request, municipality_slug):
    municipality = get_object_or_404(Municipality, slug=municipality_slug)
    category_pages = CategoryPage.objects.filter(municipality=municipality).select_related('category')
    categories = [page.category for page in category_pages]

    return render(request, "page/municipality.html", {
        "municipality": municipality,
        "department": municipality.department,
        "categories": categories,
    })

# Muestra la página de una categoría: su introducción y la lista de ítems
def category_page_view(request, municipality_slug, category_slug):
    page = get_object_or_404(
        CategoryPage,
        municipality__slug=municipality_slug,
        category__slug=category_slug
    )
    
    items = page.items.filter(published=True)

    context = {
        'page': page,
        'items': items,
        'municipality': page.municipality,
        'category': page.category,
    }
    return render(request, 'page/category_page.html', context)

# Muestra el detalle de un ítem de contenido específico relacionado a un municipio.
def content_item_detail(request, municipality_slug, category_slug, item_slug):
    item = get_object_or_404(
        ContentItem,
        slug=item_slug,
        page__municipality__slug=municipality_slug,
        page__category__slug=category_slug,
        published=True
    )
    context = {
        'item': item,
        'page': item.page,
        'municipality': item.municipality,
        'category': item.category,
    }
    return render(request, 'page/content_item_detail.html', context)

# Muestra los detalles de un evento.
def event_detail(request, event_slug):
    event = get_object_or_404(Event, slug=event_slug, published=True)
    return render(request, 'page/event_detail.html', {'event': event})

# La barra de búsqueda busca de departamentos, municipios e ítems de contenido.
def view_search(request):
    query = request.GET.get('search','').strip()
    departments = []
    municipalities = []
    content_items = []

    if query:
        departments = Department.objects.filter(name__icontains=query)
        municipalities = Municipality.objects.filter(name__icontains=query)
        content_items = ContentItem.objects.filter(title__icontains=query,published=True)

    return render(request, 'page/search.html',{
        'query': query,
        'departments': departments,
        'municipalities': municipalities,
        'content_items': content_items,
    })
    


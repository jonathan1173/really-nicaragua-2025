from django import template
from django.urls import reverse

register = template.Library()

@register.inclusion_tag('components/breadcrumb.html', takes_context=True)
def render_breadcrumb(context):
    request = context['request']
    breadcrumb = []
    breadcrumb.append({'name': 'Home', 'url': reverse('page-home')})
    breadcrumb.append({'name': 'Mapa', 'url': reverse('home-maps')})

    # Extraer los objetos principales del contexto de la vista
    item = context.get('item')
    page = context.get('page')
    municipality = context.get('municipality')
    department = context.get('department')

    # Reconstruir la jerarquía desde el objeto más específico
    # para asegurar el orden correcto del breadcrumb.
    if item:
        page = item.page
        municipality = page.municipality
        department = municipality.department
    elif page:
        municipality = page.municipality
        department = municipality.department
    elif municipality:
        department = municipality.department

    # Construir la lista de breadcrumbs usando los métodos get_absolute_url
    if department:
        breadcrumb.append({
            'name': department.name,
            'url': department.get_absolute_url()
        })
    if municipality:
        breadcrumb.append({
            'name': municipality.name,
            'url': municipality.get_absolute_url()
        })
    if page:
        breadcrumb.append({
            'name': page.category.name,
            'url': page.get_absolute_url()
        })
    if item:
        breadcrumb.append({'name': item.title, 'url': item.get_absolute_url()})

    # El último elemento del breadcrumb no debe ser un enlace
    if breadcrumb:
        breadcrumb[-1]['url'] = None

    return {'breadcrumb': breadcrumb}

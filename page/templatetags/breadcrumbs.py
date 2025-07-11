from django import template
from django.urls import reverse

register = template.Library()

@register.inclusion_tag('components/breadcrumb.html', takes_context=True)
def render_breadcrumb(context):
    request = context['request']
    path = request.path
    breadcrumb = []    
    breadcrumb.append({'name': 'Home', 'url': '/home'})
    
    if path.startswith('/home/maps'):
        breadcrumb.append({'name': 'Maps', 'url': reverse('home-maps')})


    if 'department' in context:
        dept = context['department']
        if dept:
            breadcrumb.append({
                'name': dept.name,
                'url': reverse('maps-department', args=[dept.name])
            })

    if 'municipality' in context:
        muni = context['municipality']
        breadcrumb.append({
            'name': muni.name,
            'url': reverse('municipality-options', args=[muni.name])
        })

    if 'category' in context:
        breadcrumb.append({'name': context['category'].title(), 'url': None})

    return {'breadcrumb': breadcrumb}


from django.urls import path
from .views import (
    page_index, 
    page_home, 
    page_maps, 
    page_department, 
    municipality_detail, 
    category_page_view,
    content_item_detail,
    view_search
)

urlpatterns = [
    path('', page_index , name='page-index'),
    path('home/', page_home, name='page-home'),
    path('home/maps/', page_maps, name="home-maps"),
    
    # URL para un departamento específico, que muestra sus municipios
    # Ejemplo: /home/maps/granada/
    path('home/maps/<slug:department_slug>/', page_department, name='maps-department'),
    
    # URL para un municipio específico, que muestra sus categorías de contenido
    # Ejemplo: /home/maps/municipality/granada/
    path('home/maps/municipality/<slug:municipality_slug>/', municipality_detail, name='municipality-detail'),
    
    # URL para la página de una categoría, que muestra la introducción y la lista de ítems
    # Ejemplo: /home/maps/granada/gastronomia/
    path('home/maps/<slug:municipality_slug>/<slug:category_slug>/', category_page_view, name='category-page'),
    
    # URL para la página de detalle de un ítem de contenido específico
    # Ejemplo: /home/maps/granada/gastronomia/vigoron/
    path('home/maps/<slug:municipality_slug>/<slug:category_slug>/<slug:item_slug>/', content_item_detail, name='content-item-detail'),
    
    path('home/search/', view_search, name='page-search')
]

from django.urls import path
from .views import page_index, page_home, page_maps, page_department, municipality_options, municipality_content

urlpatterns = [
    path('', page_index , name='page-index'),
    path('home/', page_home, name='page-home'),
    path('home/maps', page_maps, name="home-maps"),
    path('home/maps/<str:city>', page_department, name='maps-department'),
    path('home/maps/<str:municipality_name>/options', municipality_options, name='municipality-options'),
    path('home/maps/<str:municipality_name>/content/<str:category>', municipality_content, name='municipality-content'),
]
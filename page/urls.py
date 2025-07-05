from django.urls import path
from .views import page_index, page_home

urlpatterns = [
    path('', page_index , name='page-index '),
    path('home/', page_home, name='page-home'),

]
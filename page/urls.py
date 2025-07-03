from django.urls import path
from .views import page_index

urlpatterns = [
    path('', page_index , name='index ')
]
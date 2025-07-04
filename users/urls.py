from django.urls import path
from .views import page_register, page_login

urlpatterns = [
    path('register', page_register , name='users-register'),
    path('login', page_login, name='users-login' ),
]
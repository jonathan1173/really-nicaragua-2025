from django.urls import path
from .views import page_register, page_login, logout_view

urlpatterns = [
    path('register', page_register , name='users-register'),
    path('login', page_login, name='users-login' ),
    path('logout', logout_view, name='users-logout')

]
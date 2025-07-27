from django.urls import path
from .views import page_register, page_login, logout_view, view_profile, toggle_favorite, is_favorite

urlpatterns = [
    path('register', page_register , name='users-register'),
    path('login', page_login, name='users-login' ),
    path('logout', logout_view, name='users-logout'),
    path('profile',view_profile, name='users-profile' ),
    path('toggle-favorite/', toggle_favorite, name='toggle-favorite'),
    path('is-favorite/', is_favorite, name='is-favorite'),


]
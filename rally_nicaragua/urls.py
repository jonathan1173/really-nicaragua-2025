from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('page.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('users/',include('users.urls')),
    path('admin/', admin.site.urls),
]

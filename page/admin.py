from django.contrib import admin
from .models import Municipality, Department, Content, Category

admin.site.register(Municipality)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(Content)

# Register your models here.

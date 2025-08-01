from django.contrib import admin
from .models import Municipality, Department, Category , CategoryPage, ContentItem, Event

admin.site.register(Municipality)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(CategoryPage)
admin.site.register(ContentItem)
admin.site.register(Event)


from django.contrib import admin
from .models import Property

#admin.site.register(Property)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'property_type', 'city', 'owner_name']
    search_fields = ['name', 'city', 'owner_name']
    list_filter = ['property_type', 'city']
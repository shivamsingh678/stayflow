from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'property', 'room_type', 'capacity', 'rent']
    search_fields = ['room_number']
    list_filter = ['room_type', 'is_available']
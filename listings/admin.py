from django.contrib import admin
from .models import Plot

@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    # This determines what columns you see in the main list
    list_display = ('district', 'village', 'dimensions', 'price', 'is_verified')
    
    # This adds a sidebar to filter by district or verification status
    list_filter = ('district', 'is_verified')
    
    # This adds a search bar at the top to search by village or description
    search_fields = ('district', 'village', 'description')
    
    # This allows you to click 'is_verified' directly in the list to change it
    list_editable = ('is_verified',)

    # Organizes the detail page when you click to edit a plot
    fieldsets = (
        ("Location Info", {
            'fields': ('district', 'village', 'google_maps_link')
        }),
        ("Property Details", {
            'fields': ('dimensions', 'price', 'description', 'main_image')
        }),
        ("Status", {
            'fields': ('is_verified',)
        }),
    )
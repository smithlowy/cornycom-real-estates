from rest_framework import serializers
from .models import Plot

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = ['id', 'dimensions', 'price', 'district', 'village', 'main_image', 'google_maps_link', 'description', 'is_verified']
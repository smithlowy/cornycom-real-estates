from rest_framework import generics
from .models import Plot
from .serializers import PlotSerializer

# This view handles both returning all plots and searching
class PlotListAPIView(generics.ListAPIView):
    serializer_class = PlotSerializer

    def get_queryset(self):
        queryset = Plot.objects.all()
        district = self.request.query_params.get('district')
        if district is not None:
            queryset = queryset.filter(district__icontains=district)
        return queryset